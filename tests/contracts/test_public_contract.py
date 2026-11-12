"""Exercise the installed distribution with mocked HTTP, including sync and async clients."""

import json
from importlib import resources
from uuid import UUID

import httpx
import pytest

from soferai import AsyncSoferAI, SoferAI
from soferai.ocr.types.ocr_document_create_request import OcrDocumentCreateRequest
from soferai.transcribe.types.batch_audio_source import BatchAudioSource
from soferai.transcribe.types.batch_manifest_audio_source import BatchManifestAudioSource
from soferai.transcribe.types.batch_transcription_request_info import BatchTranscriptionRequestInfo
from soferai.transcribe.types.transcription_request_info import TranscriptionRequestInfo

DOCUMENT_ID = "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"
BATCH_ID = "a1b2c3d4-e5f6-4890-abcd-ef1234567890"
FOLDER_ID = "b1b2c3d4-e5f6-4890-abcd-ef1234567890"
API_SOURCE = json.loads(resources.files("soferai").joinpath("api_source.json").read_text())
OCR_MODES = API_SOURCE["ocr_modes"]


@pytest.mark.parametrize("model", [TranscriptionRequestInfo, BatchTranscriptionRequestInfo])
def test_transcription_settings_are_declared_fields(model):
    # extra="allow" alone must never make an old generated client pass this gate.
    assert {
        "transliteration_style",
        "hebrew_word_format",
        "auto_detect_speakers",
        "folder_id",
    } <= model.model_fields.keys()
    info = model(
        primary_language="en",
        hebrew_word_format=["hybrid"],
        transliteration_style="ashkenazi",
        auto_detect_speakers=True,
        folder_id=UUID(FOLDER_ID),
    )
    assert info.model_dump(mode="json", exclude_unset=True) == {
        "primary_language": "en",
        "hebrew_word_format": ["hybrid"],
        "transliteration_style": "ashkenazi",
        "auto_detect_speakers": True,
        "folder_id": FOLDER_ID,
    }


@pytest.mark.parametrize("model", [BatchAudioSource, BatchManifestAudioSource])
def test_batch_item_identifiers_and_speaker_overrides_are_typed(model):
    assert {"client_item_id", "num_speakers", "auto_detect_speakers"} <= model.model_fields.keys()


def test_ocr_modes_are_typed():
    assert "folder_id" in OcrDocumentCreateRequest.model_fields
    if len(OCR_MODES) > 1:
        assert "mode" in OcrDocumentCreateRequest.model_fields
        for mode in OCR_MODES:
            request = OcrDocumentCreateRequest(file="AA==", file_name="page.png", content_type="image/png", mode=mode)
            assert request.model_dump()["mode"] == mode
    else:
        assert "mode" not in OcrDocumentCreateRequest.model_fields


def test_distribution_contains_api_generation_provenance():
    source = json.loads(resources.files("soferai").joinpath("api_source.json").read_text())
    assert source["repository"] == "SoferAi/app"
    assert len(source["commit"]) == 40
    assert len(source["schema_sha256"]) == 64


def respond(request: httpx.Request) -> httpx.Response:
    assert request.headers["Authorization"] == "Bearer sdk-contract-test"
    path = request.url.path
    if path == "/v1/transcriptions/":
        body = json.loads(request.content)
        assert body["info"]["transliteration_style"] == "ashkenazi"
        assert body["info"]["hebrew_word_format"] == ["hybrid"]
        assert body["info"]["auto_detect_speakers"] is True
        assert body["info"]["folder_id"] == FOLDER_ID
        return httpx.Response(200, json=DOCUMENT_ID)
    if path == "/v1/transcriptions/batch":
        body = json.loads(request.content)
        assert body["info"]["transliteration_style"] == "ashkenazi"
        assert body["info"]["hebrew_word_format"] == ["hybrid"]
        if body["processing_mode"] == "standard":
            assert body["batch_file_id"] == DOCUMENT_ID
            assert "audio_sources" not in body
        else:
            assert body["audio_sources"][0]["client_item_id"] == "lecture-1"
            assert body["audio_sources"][0]["num_speakers"] == 2
        return httpx.Response(
            200, json={"batch_id": BATCH_ID, "transcription_ids": [DOCUMENT_ID], "total_count": 1, "status": "RECEIVED"}
        )
    if path == f"/v1/transcriptions/batch-files/{DOCUMENT_ID}/batches":
        assert request.url.params["limit"] == "10"
        return httpx.Response(
            200,
            json={
                "batch_file_id": DOCUMENT_ID,
                "total_count": 0,
                "batches": [],
                "limit": 10,
                "offset": 0,
                "has_more": False,
            },
        )
    if path == f"/v1/transcriptions/batch/{BATCH_ID}/items/by-client-item-id":
        assert request.url.params["client_item_id"] == "lecture-1"
        return httpx.Response(
            200,
            json={
                "id": DOCUMENT_ID,
                "title": "lecture",
                "created_at": "2026-11-12T00:00:00Z",
                "status": "COMPLETED",
                "client_item_id": "lecture-1",
            },
        )
    if path == "/v1/ocr/" and request.method == "POST":
        body = json.loads(request.content)
        assert body.get("mode", "standard") in OCR_MODES
        assert body["folder_id"] == FOLDER_ID
        return httpx.Response(
            200, json={"document_id": DOCUMENT_ID, "status": "PENDING", "num_pages": 1, "estimated_api_cost_cents": 2.5}
        )
    if path == f"/v1/ocr/{DOCUMENT_ID}":
        return httpx.Response(
            200,
            json={
                "document_id": DOCUMENT_ID,
                "title": "page",
                "completed_pages": 1,
                "failed_pages": 0,
                "status": "COMPLETED",
                "pages": [],
            },
        )
    raise AssertionError(f"Unexpected SDK request: {request.method} {request.url}")


def settings():
    return {
        "primary_language": "en",
        "hebrew_word_format": ["hybrid"],
        "transliteration_style": "ashkenazi",
        "folder_id": UUID(FOLDER_ID),
        "auto_detect_speakers": True,
    }


def test_sync_requests_preserve_public_api_contract():
    with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
        client = SoferAI(api_key="sdk-contract-test", httpx_client=transport)
        assert (
            str(
                client.transcribe.create_transcription(
                    audio_url="https://example.com/audio.mp3", info=TranscriptionRequestInfo(**settings())
                )
            )
            == DOCUMENT_ID
        )
        assert (
            client.batch_transcribe.create_batch_transcription(
                info=BatchTranscriptionRequestInfo(**settings()),
                processing_mode="standard",
                batch_file_id=UUID(DOCUMENT_ID),
            ).total_count
            == 1
        )
        assert (
            client.batch_transcribe.create_batch_transcription(
                info=BatchTranscriptionRequestInfo(**settings()),
                processing_mode="express",
                audio_sources=[
                    BatchAudioSource(
                        audio_url="https://example.com/audio.mp3", client_item_id="lecture-1", num_speakers=2
                    )
                ],
            ).total_count
            == 1
        )
        assert client.batch_transcribe.list_batch_file_batches(UUID(DOCUMENT_ID), limit=10).total_count == 0
        assert (
            str(
                client.batch_transcribe.get_batch_transcription_by_client_item_id(
                    UUID(BATCH_ID), client_item_id="lecture-1"
                ).id
            )
            == DOCUMENT_ID
        )
        for mode in OCR_MODES:
            assert (
                str(
                    client.ocr.create_ocr_document(
                        file="AA==",
                        file_name="page.png",
                        content_type="image/png",
                        **({"mode": mode} if len(OCR_MODES) > 1 else {}),
                        folder_id=UUID(FOLDER_ID),
                    ).document_id
                )
                == DOCUMENT_ID
            )
        assert client.ocr.get_ocr_document(UUID(DOCUMENT_ID)).status == "COMPLETED"


@pytest.mark.asyncio
async def test_async_requests_preserve_public_api_contract():
    async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as transport:
        client = AsyncSoferAI(api_key="sdk-contract-test", httpx_client=transport)
        assert (
            str(
                await client.transcribe.create_transcription(
                    audio_url="https://example.com/audio.mp3", info=TranscriptionRequestInfo(**settings())
                )
            )
            == DOCUMENT_ID
        )
        assert (
            await client.batch_transcribe.create_batch_transcription(
                info=BatchTranscriptionRequestInfo(**settings()),
                processing_mode="standard",
                batch_file_id=UUID(DOCUMENT_ID),
            )
        ).total_count == 1
        assert (
            await client.batch_transcribe.create_batch_transcription(
                info=BatchTranscriptionRequestInfo(**settings()),
                processing_mode="express",
                audio_sources=[
                    BatchAudioSource(
                        audio_url="https://example.com/audio.mp3", client_item_id="lecture-1", num_speakers=2
                    )
                ],
            )
        ).total_count == 1
        assert (await client.batch_transcribe.list_batch_file_batches(UUID(DOCUMENT_ID), limit=10)).total_count == 0
        assert (
            str(
                (
                    await client.batch_transcribe.get_batch_transcription_by_client_item_id(
                        UUID(BATCH_ID), client_item_id="lecture-1"
                    )
                ).id
            )
            == DOCUMENT_ID
        )
        for mode in OCR_MODES:
            assert (
                str(
                    (
                        await client.ocr.create_ocr_document(
                            file="AA==",
                            file_name="page.png",
                            content_type="image/png",
                            **({"mode": mode} if len(OCR_MODES) > 1 else {}),
                            folder_id=UUID(FOLDER_ID),
                        )
                    ).document_id
                )
                == DOCUMENT_ID
            )
        assert (await client.ocr.get_ocr_document(UUID(DOCUMENT_ID))).status == "COMPLETED"
