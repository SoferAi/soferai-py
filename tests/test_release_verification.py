"""Prove publication checks reject a stale wheel and a broken release handoff."""

import base64
import hashlib
import io
import json
import zipfile
from datetime import datetime, timezone

import pytest

from scripts import check_published
from scripts.check_live_api import ROUTES, mismatches
from scripts.check_published import differences, pending_prs, validate_source, wheel_files


def make_wheel(files):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as wheel:
        for name, content in files.items():
            wheel.writestr(f"soferai/{name}", content)
        wheel.writestr("soferai-1.3.0.dist-info/METADATA", "Name: soferai\nVersion: 1.3.0")
    blob = stream.getvalue()
    return blob, hashlib.sha256(blob).hexdigest()


def test_published_payload_must_match_source_including_removed_files():
    expected = {"client.py": b"new", "api_source.json": b"source", "py.typed": b""}
    blob, digest = make_wheel(expected)
    assert differences(expected, wheel_files(blob, digest)) == []
    stale, digest = make_wheel({"client.py": b"old", "removed_endpoint.py": b"old"})
    assert differences(expected, wheel_files(stale, digest)) == [
        "api_source.json",
        "client.py",
        "py.typed",
        "removed_endpoint.py",
    ]


def test_wheel_integrity_failure_is_not_accepted():
    blob, _ = make_wheel({"client.py": b"new"})
    with pytest.raises(ValueError, match="SHA-256"):
        wheel_files(blob, "0" * 64)


def test_generation_provenance_is_required():
    with pytest.raises(ValueError, match="provenance"):
        validate_source({})
    source = {"repository": "SoferAi/app", "commit": "a" * 40, "schema_sha256": "b" * 64}
    assert validate_source({"api_source.json": json.dumps(source).encode()}) == source
    source["commit"] = "main"
    with pytest.raises(ValueError, match="immutable"):
        validate_source({"api_source.json": json.dumps(source).encode()})


def test_superseded_generated_prs_do_not_keep_monitor_red_after_a_release():
    published = datetime(2026, 11, 12, 15, tzinfo=timezone.utc)
    old = {"head": {"ref": "fern-bot/old"}, "updated_at": "2026-11-12T14:00:00Z"}
    pending = {"head": {"ref": "fern-bot/new"}, "updated_at": "2026-11-12T16:00:00Z"}
    release = {
        "head": {"ref": "release-please--branches--main"},
        "updated_at": "2026-11-12T16:00:00Z",
        "labels": [{"name": "autorelease: pending"}],
    }
    unrelated = {"head": {"ref": "renovate/httpx"}, "updated_at": "2026-11-12T16:00:00Z"}
    assert pending_prs([old, pending, release, unrelated], published) == [pending, release]


def test_api_drift_is_detected_even_without_a_generation_pr(monkeypatch):
    monkeypatch.setenv("API_SOURCE_TOKEN", "test-read-token")
    content = {"fern/definition/api.yml": b"types: {}\n", "fern/generators.yml": b"groups: {}\n"}

    def read(url, **kwargs):
        if url.endswith("/releases/latest"):
            return json.dumps({"tag_name": "api-v1", "published_at": "2026-11-10T00:00:00Z"}).encode()
        if url.endswith("/commits/api-v1"):
            return json.dumps({"sha": "a" * 40}).encode()
        if "/commits?path=" in url:
            return json.dumps([{"commit": {"committer": {"date": "2026-11-10T00:00:00Z"}}}]).encode()
        path = url.split("/contents/")[1].split("?")[0]
        if path == "fern/definition":
            return json.dumps([{"path": "fern/definition/api.yml", "type": "file"}]).encode()
        return json.dumps({"content": base64.b64encode(content[path]).decode()}).encode()

    monkeypatch.setattr(check_published, "read_url", read)
    now = datetime(2026, 11, 12, tzinfo=timezone.utc)
    _, failures = check_published.api_source_status({"schema_sha256": "outdated"}, 24, now)
    assert len(failures) == 1
    assert "Released API schema differs" in failures[0]
    digest = hashlib.sha256()
    for path, blob in sorted(content.items()):
        digest.update(path.encode() + b"\0" + blob + b"\0")
    report, failures = check_published.api_source_status({"schema_sha256": digest.hexdigest()}, 24, now)
    assert failures == []
    assert report == ["API schema fingerprint matches API release api-v1"]


def test_unreleased_sdk_fields_block_publication():
    live = {
        "paths": {path: {method: {}} for path, method in ROUTES.items()},
        "components": {"schemas": {"OcrDocumentCreateRequest": {"properties": {"file": {}}}}},
    }
    assert mismatches({"OcrDocumentCreateRequest": {"file"}}, live) == []
    assert mismatches({"OcrDocumentCreateRequest": {"file", "mode"}}, live) == [
        "Live OcrDocumentCreateRequest does not accept SDK fields: mode"
    ]
