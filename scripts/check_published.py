"""Compare the actual PyPI wheel with the SDK source and monitor release handoffs."""

from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = "soferai"


def read_url(url: str, *, token: str | None = None) -> bytes:
    if not url.startswith("https://"):
        raise ValueError("Release verification requires HTTPS")
    headers = {"User-Agent": "soferai-sdk-release-verification"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)  # noqa: S310 -- HTTPS is required above.
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 -- HTTPS is required above.
        return response.read()


def package_files(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file() and path.suffix in {".py", ".json", ".typed"} and "__pycache__" not in path.parts
    }


def wheel_files(blob: bytes, expected_sha256: str) -> dict[str, bytes]:
    if hashlib.sha256(blob).hexdigest() != expected_sha256:
        raise ValueError("Downloaded wheel does not match its PyPI SHA-256")
    with zipfile.ZipFile(io.BytesIO(blob)) as wheel:
        return {
            name[len(PACKAGE) + 1 :]: wheel.read(name)
            for name in wheel.namelist()
            if name.startswith(f"{PACKAGE}/") and Path(name).suffix in {".py", ".json", ".typed"}
        }


def differences(expected: dict[str, bytes], actual: dict[str, bytes]) -> list[str]:
    return sorted(name for name in expected.keys() | actual.keys() if expected.get(name) != actual.get(name))


def validate_source(files: dict[str, bytes]) -> dict[str, str]:
    source = json.loads(files.get("api_source.json", b"{}"))
    if source.get("repository") != "SoferAi/app":
        raise ValueError("SDK is missing API generation provenance")
    if not re.fullmatch(r"[a-f0-9]{40}", source.get("commit", "")):
        raise ValueError("SDK API source commit must be an immutable SHA")
    if not re.fullmatch(r"[a-f0-9]{64}", source.get("schema_sha256", "")):
        raise ValueError("SDK API schema fingerprint is missing or invalid")
    return source


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def pending_prs(pulls: list[dict], published_at: datetime) -> list[dict]:
    """Ignore superseded regeneration PRs last updated before the latest publication."""
    return [
        pull
        for pull in pulls
        if parse_time(pull["updated_at"]) > published_at
        and (
            pull["head"]["ref"].startswith("fern-bot/")
            or any(label["name"] == "autorelease: pending" for label in pull.get("labels", []))
        )
    ]


def github_handoffs(published_at: datetime, grace_hours: float, now: datetime) -> list[str]:
    token = os.getenv("GITHUB_TOKEN")
    repository = os.getenv("GITHUB_REPOSITORY")
    if not token or not repository:
        return []
    if repository.lower() != "soferai/soferai-py":
        raise ValueError("Freshness monitor must run in the Python SDK repository")
    api = f"https://api.github.com/repos/{repository}"
    pulls = json.loads(read_url(f"{api}/pulls?state=open&sort=updated&direction=desc&per_page=100", token=token))
    failures = []
    for pull in pending_prs(pulls, published_at):
        age_hours = (now - parse_time(pull["created_at"])).total_seconds() / 3600
        checks = json.loads(read_url(f"{api}/commits/{pull['head']['sha']}/check-runs?per_page=100", token=token))
        # A later rerun replaces an earlier result with the same check name.
        latest = {}
        for check in reversed(checks.get("check_runs", [])):
            latest[check["name"]] = check
        broken = [
            check["name"]
            for check in latest.values()
            if check.get("conclusion") in {"failure", "timed_out", "cancelled"}
        ]
        if broken:
            failures.append(f"{pull['html_url']}: failing checks: {', '.join(broken)}")
        if age_hours > grace_hours:
            failures.append(f"{pull['html_url']}: release handoff has been open for {age_hours:.1f} hours")
    return failures


def api_source_status(source: dict[str, str], grace_hours: float, now: datetime) -> tuple[list[str], list[str]]:
    """Catch API changes even when SDK generation failed before it could open a PR."""
    token = os.getenv("API_SOURCE_TOKEN") or os.getenv("GITHUB_TOKEN")
    if not token:
        return [], []
    api = "https://api.github.com/repos/SoferAi/app"
    release = json.loads(read_url(f"{api}/releases/latest", token=token))
    head = json.loads(read_url(f"{api}/commits/{release['tag_name']}", token=token))["sha"]
    files = {}

    def collect(path):
        entries = json.loads(read_url(f"{api}/contents/{path}?ref={head}", token=token))
        for entry in entries:
            if entry["type"] == "dir":
                collect(entry["path"])
            elif entry["type"] == "file" and entry["path"].endswith(".yml"):
                item = json.loads(read_url(f"{api}/contents/{entry['path']}?ref={head}", token=token))
                files[entry["path"]] = base64.b64decode(item["content"])

    collect("fern/definition")
    generator = json.loads(read_url(f"{api}/contents/fern/generators.yml?ref={head}", token=token))
    files["fern/generators.yml"] = base64.b64decode(generator["content"])
    digest = hashlib.sha256()
    for path, content in sorted(files.items()):
        digest.update(path.encode() + b"\0" + content + b"\0")
    if digest.hexdigest() == source["schema_sha256"]:
        return [f"API schema fingerprint matches API release {release['tag_name']}"], []
    age = (now - parse_time(release["published_at"])).total_seconds() / 3600
    detail = f"Released API schema differs from this SDK: https://github.com/SoferAi/app/commit/{head}"
    if age > grace_hours:
        return [detail], [detail]
    return [detail, f"PENDING: API schema changes are within the {grace_hours:g}-hour release grace period"], []


def source_age_hours(root: Path, now: datetime) -> float:
    git = shutil.which("git")
    if not git:
        raise ValueError("git is required to determine the SDK source age")
    timestamp = subprocess.check_output(  # noqa: S603 -- Fixed git arguments; no shell.
        [git, "log", "-1", "--format=%cI", "--", "src/soferai"],
        cwd=root,
        text=True,
    ).strip()
    if not timestamp:
        raise ValueError("Cannot determine SDK source age; checkout needs git history")
    return (now - parse_time(timestamp)).total_seconds() / 3600


def check(root: Path, version: str | None, grace_hours: float, *, handoffs: bool = True) -> tuple[list[str], list[str]]:
    now = datetime.now(timezone.utc)
    expected = package_files(root / "src" / PACKAGE)
    source = validate_source(expected)
    url = f"https://pypi.org/pypi/{PACKAGE}/{version}/json" if version else f"https://pypi.org/pypi/{PACKAGE}/json"
    release = json.loads(read_url(url))
    wheel = next(item for item in release["urls"] if item["packagetype"] == "bdist_wheel")
    actual = wheel_files(read_url(wheel["url"]), wheel["digests"]["sha256"])
    changed = differences(expected, actual)
    report = [
        f"PyPI version: {release['info']['version']}",
        f"API source: https://github.com/{source['repository']}/commit/{source['commit']}",
        f"API schema SHA-256: {source['schema_sha256']}",
        f"Verified wheel SHA-256: {wheel['digests']['sha256']}",
    ]
    failures = []
    if changed:
        age = source_age_hours(root, now) if grace_hours else float("inf")
        detail = f"Published package differs in {len(changed)} files: {', '.join(changed[:12])}"
        report.append(detail)
        if age > grace_hours:
            failures.append(detail)
        else:
            report.append(f"PENDING: source changes are within the {grace_hours:g}-hour release grace period")
    else:
        validate_source(actual)
        report.append("CURRENT: published wheel matches every SDK Python file, package marker, and API provenance file")
    if handoffs:
        failures.extend(github_handoffs(parse_time(wheel["upload_time_iso_8601"]), grace_hours, now))
        api_report, api_failures = api_source_status(source, grace_hours, now)
        report.extend(api_report)
        failures.extend(api_failures)
    return report, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", help="Verify an exact newly published version instead of PyPI latest")
    parser.add_argument(
        "--grace-hours", type=float, default=0, help="Scheduled monitor grace period for source changes"
    )
    parser.add_argument("--attempts", type=int, default=1, help="Retry bounded PyPI propagation checks")
    parser.add_argument("--delay", type=float, default=10)
    parser.add_argument("--no-handoffs", action="store_true", help="Verify a package without scanning open PRs")
    args = parser.parse_args()
    report = []
    failures = []
    for attempt in range(max(1, args.attempts)):
        try:
            report, failures = check(ROOT, args.version, args.grace_hours, handoffs=not args.no_handoffs)
        except (OSError, ValueError, KeyError, StopIteration, zipfile.BadZipFile) as error:
            failures = [f"Release verification could not complete: {error}"]
        if not failures or attempt + 1 == args.attempts:
            break
        time.sleep(args.delay)
    lines = ["## Python SDK publication", *[f"- {line}" for line in report], *[f"- ERROR: {line}" for line in failures]]
    print("\n".join(lines))
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with Path(summary).open("a") as file:
            file.write("\n".join(lines) + "\n")
    return int(bool(failures))


if __name__ == "__main__":
    sys.exit(main())
