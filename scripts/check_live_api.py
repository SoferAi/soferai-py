"""Read the live OpenAPI schema before publishing an SDK; never submit processing jobs."""

import importlib
import json
import sys
import urllib.request

MODELS = {
    "TranscriptionRequestInfo": "soferai.transcribe.types.transcription_request_info",
    "BatchTranscriptionRequestInfo": "soferai.transcribe.types.batch_transcription_request_info",
    "BatchAudioSource": "soferai.transcribe.types.batch_audio_source",
    "OcrDocumentCreateRequest": "soferai.ocr.types.ocr_document_create_request",
}
ROUTES = {
    "/v1/transcriptions/batch-files/{batch_file_id}/batches": "get",
    "/v1/transcriptions/batch/{batch_id}/items/by-client-item-id": "get",
    "/v1/ocr/": "post",
    "/v1/ocr/{document_id}": "get",
}


def mismatches(models, schema):
    errors = []
    available = schema.get("components", {}).get("schemas", {})
    for name, fields in models.items():
        missing = fields - available.get(name, {}).get("properties", {}).keys()
        if missing:
            errors.append(f"Live {name} does not accept SDK fields: {', '.join(sorted(missing))}")
    for path, method in ROUTES.items():
        if method not in schema.get("paths", {}).get(path, {}):
            errors.append(f"Live API is missing {method.upper()} {path}")
    return errors


def main():
    request = urllib.request.Request(
        "https://api.sofer.ai/openapi.json", headers={"User-Agent": "soferai-sdk-release-verification"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 -- Fixed HTTPS API origin.
        schema = json.load(response)
    models = {name: set(getattr(importlib.import_module(module), name).model_fields) for name, module in MODELS.items()}
    errors = mismatches(models, schema)
    if errors:
        print("SDK publication is blocked until the live API supports its request contract:")
        print("\n".join(errors))
    else:
        print("Live API accepts the SDK's transcription settings, batch item lookups, and public OCR request fields.")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
