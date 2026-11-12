# Keeping the Python SDK current

Zach owns the Python SDK release handoff. Public API changes generate a reviewed SDK PR from `SoferAi/app`.
The app's generation workflow records its immutable API source commit and schema fingerprint in
`src/soferai/api_source.json`. Fern preserves that file, release tooling, and contract tests through `.fernignore`.

For every public API release:

1. Check the generated PR's API provenance against the intended API release. Review removed methods, fields,
   and changed required arguments. Use a conventional `feat(api)!:` title and describe migration steps for
   breaking changes; use `feat(api):` for compatible additions. The automatic title normalization only fixes
   Fern's default title and does not classify breaking changes.
2. Require green quality checks, public request contract tests, the Python/OS matrix, and a wheel build.
   CI uses mocked HTTP without production credentials. It validates declared typed fields as well as
   actual sync/async request bodies and routes. Source imports alone do not establish wheel correctness.
3. Merge the validated generation PR. The verified main build runs release-please, which opens or updates
   a version PR after a read-only live OpenAPI check confirms the generated request fields and routes are
   deployed. Review and merge that version PR to create the release and publish its already-tested
   distributions through the existing PyPI environment and trusted publisher.
4. Verify the `Verify the package customers install` job: it checks the PyPI wheel checksum, compares all
   SDK source/provenance files, installs that exact version from public PyPI into a fresh environment, and
   repeats the public request contracts. Align newly exposed SDK capabilities with the intended API rollout.
   SDK tests do not deploy the API, activate products, or establish live billing readiness.

The daily **Python SDK freshness** workflow has read-only permissions. It compares PyPI's actual wheel to main
and reports the API commit and schema fingerprint in its job summary. Source drift has a 24-hour release grace
period and is explicitly reported as pending during that period. Failed checks on pending generation/release PRs
fail the monitor immediately; handoffs open longer than 24 hours also fail. Superseded PRs last updated before
the latest publication are ignored. GitHub Actions failure notifications and the workflow summary are the
visible failure signal; inspect this workflow after API changes until the version is published. It also compares
the latest released API definition's fingerprint using a read-only bot token, so a failed generation job with no new
SDK PR cannot hide an API change. API definition drift has the same 24-hour grace period.

Run the exact package check locally with `python scripts/check_published.py --version VERSION --no-handoffs`.
It performs read-only PyPI requests. It never publishes, merges, or submits processing jobs. A successful
generation job alone is not evidence that the client installed by customers is current.

## Migration for the current API regeneration

The public OCR client now uses `client.ocr.create_ocr_document(...)` and
`client.ocr.get_ocr_document(document_id)`, with one durable document ID. Available OCR modes are recorded in
`api_source.json` and follow the released server; unreleased modes must wait for the server rollout.
These methods replace the older `create_ocr_job`/`get_ocr_job` methods. Use a major SDK version
for this removal. Standard/Express transcription callers can retain their existing batch flows and gain
typed transliteration, folders, speaker auto-detection, and per-item client identifiers.
