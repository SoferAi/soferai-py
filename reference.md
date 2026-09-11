# Reference
## Balance
<details><summary><code>client.balance.<a href="src/soferai/balance/client.py">get_balance</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get account balance showing available balance and pending charges
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.balance.get_balance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BatchTranscribe
<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">create_batch_transcription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple transcriptions in a single batch request.

**Choose a processing mode:**

- **Express mode**: Submit up to 10 files at once with `audio_sources`. Express batches may take longer than individual transcription requests, but make it easier to submit multiple files together. Pricing for v1 is $1.50/hour.
- **Standard mode**: Transcriptions processed within 24 hours. Max 500 files. Lower cost. First upload a manifest via [Upload Batch Manifest File](/api-reference/batch-transcribe/upload-batch-file), then pass the `batch_file_id` here. Pricing for v1 batch standard is $1.00/hour. If you need higher limits, contact support@sofer.ai.

All files in the batch share the same transcription settings (model, language, etc.) defined in `info`.

Speaker settings can be provided at the batch level or per item. Per-item `num_speakers` or `auto_detect_speakers` settings take precedence over the batch-level speaker settings in `info`. If an item omits both speaker fields, it inherits the batch-level setting. If neither level provides a speaker setting, the transcription defaults to one speaker. Do not provide both `num_speakers` and `auto_detect_speakers` in the same object.

If you include a `client_item_id` on each item, it must be unique within the batch. You can later resolve a `client_item_id` back to the canonical transcription ID with [Get Batch Transcription By Client Item ID](/api-reference/batch-transcribe/get-batch-transcription-by-client-item-id).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI
from soferai.transcribe import BatchTranscriptionRequestInfo

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.create_batch_transcription(
    batch_file_id=uuid.UUID(
        "f1234567-89ab-cdef-0123-456789abcdef",
    ),
    info=BatchTranscriptionRequestInfo(
        model="v1",
        primary_language="en",
        hebrew_word_format=["en", "he"],
        num_speakers=1,
    ),
    batch_title="Weekly Shiurim Collection",
    processing_mode="standard",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**info:** `BatchTranscriptionRequestInfo` 

Transcription settings applied to all files in the batch (model, language, etc.).

Batch-level speaker settings are defaults. Per-item `num_speakers` or `auto_detect_speakers` settings in `audio_sources` or a batch manifest take precedence for that item.
    
</dd>
</dl>

<dl>
<dd>

**processing_mode:** `typing.Optional[ProcessingMode]` 

Choose how the batch is processed:
- `standard` (default): Lower cost, processed within 24 hours. Max 500 files. Use with `batch_file_id`. Pricing for v1 batch standard is $1.00/hour. If you need higher limits, contact support@sofer.ai.
- `express`: Submit up to 10 files at once with `audio_sources`. Express batches may take longer than individual transcription requests, but make it easier to submit multiple files together. Pricing for v1 is $1.50/hour.
    
</dd>
</dl>

<dl>
<dd>

**batch_file_id:** `typing.Optional[uuid.UUID]` 

**For standard mode only.** ID of a previously uploaded batch manifest.

Get this by calling [Upload Batch Manifest File](/api-reference/batch-transcribe/upload-batch-file) first.
    
</dd>
</dl>

<dl>
<dd>

**audio_sources:** `typing.Optional[typing.Sequence[BatchAudioSource]]` 

**For express mode only.** List of audio URLs to transcribe (max 10).

Each item needs an `audio_url` and can optionally include a `title`, `client_item_id`, `num_speakers`, or `auto_detect_speakers`.

Per-item `num_speakers` or `auto_detect_speakers` settings take precedence over the batch-level speaker settings in `info`.

If you provide `client_item_id`, it must be unique within the batch and can be used later to look up the resulting transcription.
    
</dd>
</dl>

<dl>
<dd>

**batch_title:** `typing.Optional[str]` — Default title prefix for transcriptions. Individual items can override this. Items without titles become "{batch_title} - Item 1", "{batch_title} - Item 2", etc.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">upload_batch_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a batch manifest containing audio URLs for standard mode batch processing.

**Workflow:**
1. Upload your manifest here to get a `batch_file_id`
2. Use that ID in [Create Batch Transcription](/api-reference/batch-transcribe/create-batch-transcription) with `processing_mode: "standard"`

The manifest is a list of audio sources (max 500), each with a URL and optional title or `client_item_id`. If you provide `client_item_id`, it must be unique within the manifest. You can provide it as a JSON array or JSONL format. If you need higher limits, contact support@sofer.ai.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.upload_batch_file(
    content_type="jsonl",
    jsonl='{"audio_url": "https://example.com/shiur1.mp3", "title": "Shiur 1", "client_item_id": "shiur_1"}\n{"audio_url": "https://example.com/shiur2.mp3", "title": "Shiur 2", "client_item_id": "shiur_2"}',
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_type:** `BatchFileContentType` — Format of your manifest data
    
</dd>
</dl>

<dl>
<dd>

**json_items:** `typing.Optional[typing.Sequence[BatchManifestAudioSource]]` — **For JSON format.** Array of audio sources to transcribe (max 500). If you need higher limits, contact support@sofer.ai.
    
</dd>
</dl>

<dl>
<dd>

**jsonl:** `typing.Optional[str]` 

**For JSONL format.** One audio source per line as JSON, separated by newlines (max 500 lines). If you need higher limits, contact support@sofer.ai.

Example: `{"audio_url": "https://..."}\n{"audio_url": "https://..."}`
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[BatchFileMetadata]` — Optional title and description for this manifest
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">create_batch_file_from_rss</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a standard-mode batch manifest from a podcast RSS feed.

The feed is fetched and parsed for podcast episode audio enclosures. Each episode with an audio enclosure becomes one manifest item with `audio_url`, title, and a stable `client_item_id`. The returned `batch_file_id` can be used in [Create Batch Transcription](/api-reference/batch-transcribe/create-batch-transcription) with `processing_mode: "standard"`.

By default, this imports up to the standard batch manifest limit. Use `limit` to import fewer episodes. If the feed has more episodes than one manifest can hold, call this endpoint again with the previous response's `next_offset`.

Need to find the RSS URL for a podcast? Try the [RSS.com Podcast RSS Feed Finder](https://rss.com/tools/find-my-feed/) and use the feed URL it returns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI
from soferai.transcribe import BatchFileMetadata

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.create_batch_file_from_rss(
    rss_url="https://example.com/podcast/feed.xml",
    limit=100,
    offset=0,
    metadata=BatchFileMetadata(
        title="Weekly Parsha Podcast",
        description="Imported from RSS",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rss_url:** `str` — Public RSS feed URL to fetch and parse for podcast episode audio enclosures.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Optional maximum number of episodes to import. Defaults to the standard batch manifest limit.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of podcast episode audio enclosures to skip before importing. Use `next_offset` from the previous response to fetch the next page.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[BatchFileMetadata]` — Optional title and description for this manifest. If omitted, the podcast title from the feed is used when available.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">list_batch_files</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all batch file manifests you've uploaded. Use this to find a `batch_file_id` for starting a standard mode batch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.list_batch_files()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">get_batch_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a specific batch file manifest, including its validation status. Check this after uploading to ensure your manifest is valid before starting a batch.

To find batches already created from this manifest, use [List Batches For Manifest](/api-reference/batch-transcribe/list-batch-file-batches).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.get_batch_file(
    batch_file_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_file_id:** `uuid.UUID` — The batch file ID returned from [Upload Batch File](/api-reference/batch-transcribe/upload-batch-file)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">list_batch_file_batches</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find batches created from a specific uploaded manifest, newest first. Only manifests and batches owned by the authenticated user are returned.

Use `total_count` to check whether this manifest has ever been used to create a batch. An unused manifest returns `total_count: 0` and an empty `batches` list. A missing manifest or one owned by another user returns 404.

Each batch includes its current status and transcription counts. `RECEIVED` and `PROCESSING` indicate queued or active work; `COMPLETED` and `FAILED` indicate finished work. A completed batch can contain failed items. Use [Get Batch Status](/api-reference/batch-transcribe/get-batch-status) with a returned `batch_id` for individual transcription details.

Results match the exact `batch_file_id`, not other uploads with identical contents. This is a read-only lookup, not an atomic duplicate-submission guard.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.list_batch_file_batches(
    batch_file_id=uuid.UUID(
        "f1234567-89ab-cdef-0123-456789abcdef",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_file_id:** `uuid.UUID` — The manifest ID returned by uploading a batch file or creating one from RSS.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of batches per page. Defaults to 20; must be between 1 and 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of batches to skip. Defaults to 0; must be non-negative.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">get_batch_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the progress of a batch transcription. Returns counts of completed, failed, and pending transcriptions, plus details for each individual transcription.

If a batch item was submitted with `client_item_id`, that value is echoed back in each transcription entry.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.get_batch_status(
    batch_id=uuid.UUID(
        "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `uuid.UUID` — The batch ID returned from [Create Batch Transcription](/api-reference/batch-transcribe/create-batch-transcription)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_transcribe.<a href="src/soferai/batch_transcribe/client.py">get_batch_transcription_by_client_item_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolve a batch item's `client_item_id` to the resulting transcription.

`client_item_id` values are unique only within a batch, so this lookup is scoped by `batch_id`.

The response is a standard [TranscriptionInfo](/api-reference/transcribe/get-transcription-status) object. Its `id` field is the canonical transcription ID for the batch item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.batch_transcribe.get_batch_transcription_by_client_item_id(
    batch_id=uuid.UUID(
        "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    ),
    client_item_id="shiur_1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `uuid.UUID` — The batch ID returned from [Create Batch Transcription](/api-reference/batch-transcribe/create-batch-transcription)
    
</dd>
</dl>

<dl>
<dd>

**client_item_id:** `str` — The caller-defined client_item_id to resolve within this batch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Categories
<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">create_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new category
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.create_category(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the category
    
</dd>
</dl>

<dl>
<dd>

**color_hex:** `typing.Optional[str]` — Hex color code for the category (e.g.,
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description to help categorize transcripts.
    
</dd>
</dl>

<dl>
<dd>

**auto_tag_enabled:** `typing.Optional[bool]` — Whether to automatically tag transcripts that match this category.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">list_categories</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all categories for the authenticated user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.list_categories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">get_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific category by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.get_category(
    category_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `uuid.UUID` — ID of the category
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">update_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing category
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.update_category(
    category_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `uuid.UUID` — ID of the category to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New name for the category
    
</dd>
</dl>

<dl>
<dd>

**color_hex:** `typing.Optional[str]` — New hex color code for the category (e.g.,
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — New description for the category
    
</dd>
</dl>

<dl>
<dd>

**auto_tag_enabled:** `typing.Optional[bool]` — Whether to automatically tag transcripts that match this category
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">delete_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a category (this will also remove all transcription associations)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.delete_category(
    category_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `uuid.UUID` — ID of the category to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">add_transcription_to_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a transcription to a category
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.add_transcription_to_category(
    category_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    transcription_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `uuid.UUID` — ID of the category
    
</dd>
</dl>

<dl>
<dd>

**transcription_id:** `uuid.UUID` — ID of the transcription to add to the category
    
</dd>
</dl>

<dl>
<dd>

**position:** `typing.Optional[int]` — Optional position within the category for ordering
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">remove_transcription_from_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a transcription from a category
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.remove_transcription_from_category(
    category_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    transcription_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `uuid.UUID` — ID of the category
    
</dd>
</dl>

<dl>
<dd>

**transcription_id:** `uuid.UUID` — ID of the transcription to remove
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">get_transcription_categories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all categories for a specific transcription
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.get_transcription_categories(
    transcription_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcription_id:** `uuid.UUID` — ID of the transcription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.categories.<a href="src/soferai/categories/client.py">get_category_transcriptions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all transcriptions in a specific category
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.categories.get_category_transcriptions(
    category_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `uuid.UUID` — ID of the category
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Documents
<details><summary><code>client.documents.<a href="src/soferai/documents/client.py">create_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a durable document from plain text, Markdown, or a Word `.docx` file.

Provide exactly one of `content` or `file`. Files must be base64 encoded. Text,
Markdown, and Word ingestion completes synchronously. The returned `id` is the
document ID used by every document, translation, and folder endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.documents.create_document()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**title:** `typing.Optional[str]` — Display title. Defaults to the file name without its extension or Untitled Document.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[uuid.UUID]` — Optional owned folder. Null or omitted creates the document at root.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DocumentFormat]` — Source format. Defaults to text for content and is inferred from file_name for files.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — UTF-8 plain-text or Markdown content. Provide this or file, but not both.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[str]` — Base64-encoded `.txt`, `.md`, or `.docx` file. Provide this or content, but not both.
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` — Original file name. Used to infer format and title when those values are omitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/soferai/documents/client.py">list_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the authenticated API user's documents using cursor pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.documents.list_documents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor returned by the previous page.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents to return. Defaults to 50 and cannot exceed 100.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[uuid.UUID]` — Return only documents in this folder. Omit to list documents across all folders.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Return archived or active documents. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[DocumentFilterType]` — Optionally filter by transcript or text document type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/soferai/documents/client.py">get_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an owned document. A transcription ID returned by an existing
transcription endpoint is already a document ID; no conversion is required.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.documents.get_document(
    document_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `DocumentId` — Stable document ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/soferai/documents/client.py">update_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update document metadata. Omitted fields are unchanged. An explicitly null
`folder_id` moves the document to root; a UUID moves it into that owned folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.documents.update_document(
    document_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `DocumentId` — Stable document ID.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — New display title. Omit to leave unchanged.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[uuid.UUID]` — Omit to leave unchanged, send null to move to root, or send an owned folder UUID.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Archive or restore the document. Archived documents are moved to root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/soferai/documents/client.py">create_document_translation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a document translation. Text and transcript documents use paragraph-level
translation.

**API price:** USD 0.25 per 1,000 billable words, deducted from your API balance.
Pricing is prorated to the word: 1,000 billable words costs USD 0.25 and 10,000
billable words costs USD 2.50. Cached current paragraphs are free; stale, missing,
failed, forced, or newly added paragraphs are billable.

Repeated requests for the same document and translation configuration reuse
cached work and the same billing identity, preventing duplicate charges.

A document can have multiple translations. Each combination of target language and
translation style is stored separately, so the same document can be translated
into both English and Hebrew without duplicating the source document.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.documents.create_document_translation(
    document_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `DocumentId` — Stable document ID.
    
</dd>
</dl>

<dl>
<dd>

**target_language:** `typing.Optional[DocumentTranslationTargetLanguage]` 

Translation target language. Use `en` or `he`; omit it to use automatic
English/Hebrew direction selection. Custom styles and language-specific
built-ins require their explicit compatible target language.
    
</dd>
</dl>

<dl>
<dd>

**translation_style:** `typing.Optional[str]` 

Translation style ID. Built-ins are `default` for a clear natural translation,
`learning_english` for polished Torah-learning English, and `sefer_hebrew` for
traditional sefer-style Hebrew. Custom style IDs come from `/v1/translation-styles`.
Omit this to use `default`. `learning_english` requires target language `en`,
`sefer_hebrew` requires `he`, and each custom style declares its compatible language.
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` — Regenerate the translation even if cached content already exists.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.documents.<a href="src/soferai/documents/client.py">get_document_translation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the translation for a target language and style, including current status,
remaining billable words, estimated API cost, and translated content.

The service rebuilds the document's current paragraphs or pages and compares
their hashes with the hashes stored during translation. Changed source content
is returned as stale and becomes billable again when translation is requested.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.documents.get_document_translation(
    document_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    target_language="auto",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `DocumentId` — Stable document ID.
    
</dd>
</dl>

<dl>
<dd>

**target_language:** `DocumentTranslationTargetLanguage` — Target language used when the translation was created, or `auto` for automatic direction selection.
    
</dd>
</dl>

<dl>
<dd>

**translation_style:** `typing.Optional[str]` 

Translation style ID. Built-ins are `default`, `learning_english` for an
English target, and `sefer_hebrew` for a Hebrew target. Omit this to use
`default`. Custom style IDs come from `/v1/translation-styles`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Folders
<details><summary><code>client.folders.<a href="src/soferai/folders/client.py">create_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an owned document folder, optionally nested beneath another owned folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.folders.create_folder(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Folder name. Names are case-insensitively unique among siblings.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[uuid.UUID]` — Optional owned parent folder. Null or omitted creates a root folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/soferai/folders/client.py">list_folders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List owned folders using cursor pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.folders.list_folders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor returned by the previous page.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of folders to return. Defaults to 50 and cannot exceed 100.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[uuid.UUID]` — Return children of this folder. Omit to list all owned folders.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/soferai/folders/client.py">get_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an owned document folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.folders.get_folder(
    folder_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `uuid.UUID` — Folder ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/soferai/folders/client.py">update_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename or move a folder. Omitted fields are unchanged.
An explicitly null `parent_id` moves the folder to the root.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.folders.update_folder(
    folder_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `uuid.UUID` — Folder ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New folder name. Omit to leave unchanged.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[uuid.UUID]` — Omit to leave unchanged, null to move to root, or an owned folder UUID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/soferai/folders/client.py">delete_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an empty owned folder. This operation is non-recursive and returns 409
when the folder contains documents or child folders.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.folders.delete_folder(
    folder_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `uuid.UUID` — Folder ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.folders.<a href="src/soferai/folders/client.py">list_folder_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List owned documents directly contained by an owned folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.folders.list_folder_documents(
    folder_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `uuid.UUID` — Folder ID.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor returned by the previous page.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of documents to return. Defaults to 50 and cannot exceed 100.
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` — Return archived or active documents. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[DocumentFilterType]` — Optionally filter by document type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Health
<details><summary><code>client.health.<a href="src/soferai/health/client.py">get_health</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.health.get_health()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Link
<details><summary><code>client.link.<a href="src/soferai/link/client.py">extract</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.link.extract(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — URL to extract a downloadable link from. This link must originate from a supported site. You can use the get supported sites endpoint to get a list of supported sites.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.link.<a href="src/soferai/link/client.py">get_supported_sites</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.link.get_supported_sites()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Maishiv
<details><summary><code>client.maishiv.<a href="src/soferai/maishiv/client.py">add_to_knowledge_base</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a document to the knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.maishiv.add_to_knowledge_base(
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — ID of the document to add to the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maishiv.<a href="src/soferai/maishiv/client.py">list_knowledge_base_docs</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all document IDs currently in the knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.maishiv.list_knowledge_base_docs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.maishiv.<a href="src/soferai/maishiv/client.py">remove_from_knowledge_base</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a document from the knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.maishiv.remove_from_knowledge_base(
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — ID of the document to remove from the knowledge base.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Timestamps
<details><summary><code>client.timestamps.<a href="src/soferai/timestamps/client.py">outline</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Outline of topics discussed by timestamp, generated end-to-end from a transcription ID.

This endpoint will:
1) Fetch the transcript and word-level timestamps for the given transcription
2) Generate chapter topics (title + starting_phrase) using an LLM from the transcript text
3) Align each topic's starting phrase to timestamps
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.timestamps.outline(
    transcription_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcription_id:** `TranscriptionId` — ID of the transcription to process end-to-end
    
</dd>
</dl>

<dl>
<dd>

**monotone:** `typing.Optional[bool]` — If true, each topic is searched after the previous topic's start (with a small backoff)
    
</dd>
</dl>

<dl>
<dd>

**conclusion_bias:** `typing.Optional[bool]` — If true and a title includes the word "conclusion", search in the last third of the audio
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.timestamps.<a href="src/soferai/timestamps/client.py">update_timestamps</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the timestamps based on edited text.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI
from soferai.transcribe import Timestamp

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.timestamps.update_timestamps(
    old_timestamps=[
        Timestamp(
            word="word",
            start=1.1,
            end=1.1,
        ),
        Timestamp(
            word="word",
            start=1.1,
            end=1.1,
        ),
    ],
    edited_text="edited_text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**old_timestamps:** `typing.Sequence[Timestamp]` — The original timestamps associated with the text before editing. These will be used as reference points to align the new timestamps.
    
</dd>
</dl>

<dl>
<dd>

**edited_text:** `str` — The modified version of the transcription text that needs updated timestamp alignments. This should be the complete text after your edits.
    
</dd>
</dl>

<dl>
<dd>

**language_to_update:** `typing.Optional[Language]` — If hebrew_word_format included both 'en' and 'he' (and therefor, for the same word there is both an English and a Hebrew version),this specifies which language version of the timestamps to update. Must be either 'en' for English or 'he' for Hebrew timestamps.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transcribe
<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">create_transcription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new transcription
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI
from soferai.transcribe import TranscriptionRequestInfo

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.transcribe.create_transcription(
    info=TranscriptionRequestInfo(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**info:** `TranscriptionRequestInfo` — Transcription parameters
    
</dd>
</dl>

<dl>
<dd>

**audio_url:** `typing.Optional[str]` — URL to a downloadable audio file. Must be a direct link to the file (not a streaming or preview link). If the URL is not directly downloadable, consider using our Link API to extract a downloadable link from supported sites. Either audio_url or audio_file must be provided, but not both.
    
</dd>
</dl>

<dl>
<dd>

**audio_file:** `typing.Optional[str]` 

Base64 encoded audio file content. Either audio_url or audio_file must be provided, but not both.

## Base64 Encoding Example

**Python:**
```python
import base64
from soferai import SoferAI

# Initialize client
client = SoferAI(api_key="your_api_key_here")

# Read and encode audio file
with open("audio.mp3", "rb") as f:
    base64_audio = base64.b64encode(f.read()).decode('utf-8')

# Create transcription request
response = client.transcribe.create_transcription(
    audio_file=base64_audio,
    info={
        "model": "v1",
        "primary_language": "en",
        "hebrew_word_format": ["he"],
        "title": "My Shiur Transcription"
    }
)

print(f"Transcription ID: {response}")
```
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">get_transcription_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get transcription status
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.transcribe.get_transcription_status(
    transcription_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcription_id:** `uuid.UUID` — ID of the transcription. Use the ID returned from the Create Transcription endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">get_transcription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get transcription
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.transcribe.get_transcription(
    transcription_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcription_id:** `uuid.UUID` — ID of the transcription. Use the ID returned from the Create Transcription endpoint.
    
</dd>
</dl>

<dl>
<dd>

**filter_hebrew_word_format:** `typing.Optional[str]` 

Optionally choose a Hebrew-word rendering for the response. If set to `en`,
Hebrew characters are removed and timestamps exclude words tagged only with
`he`. If set to `he`, italicized transliterations are removed and timestamps
exclude words tagged only with `en`. If set to `hybrid`, the stored mixed
rendering is returned without `en`/`he` filtering; it does not duplicate every
Hebrew word in both formats.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">list_transcriptions</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all transcriptions for the authenticated user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.transcribe.list_transcriptions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TranslationStyles
<details><summary><code>client.translation_styles.<a href="src/soferai/translation_styles/client.py">list_translation_styles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the built-in translation styles and the authenticated API user's custom
styles. Optionally filter the result by a compatible target language.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.translation_styles.list_translation_styles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_language:** `typing.Optional[TranslationStyleTargetLanguage]` — Return only styles compatible with this target language.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.translation_styles.<a href="src/soferai/translation_styles/client.py">create_translation_style</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a reusable custom translation style. The instructions are safety-validated
and must only describe translation wording, tone, register, terminology,
transliteration, quote handling, or similar style choices. Instructions cannot
override the target language, change document structure, summarize, add content,
select a model, or alter output-format and safety rules.

Use the returned `id` directly as `translation_style` when creating a translation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.translation_styles.create_translation_style(
    name="name",
    target_language="en",
    instructions="instructions",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Display name, up to 60 characters.
    
</dd>
</dl>

<dl>
<dd>

**target_language:** `TranslationStyleTargetLanguage` — Language translations using this style will produce.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `str` — Style-only instructions, up to 4,000 characters. HTML is not accepted; use paired asterisks for emphasis.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.translation_styles.<a href="src/soferai/translation_styles/client.py">get_translation_style</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a built-in style or an owned custom translation style.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.translation_styles.get_translation_style(
    translation_style_id="translation_style_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**translation_style_id:** `str` — Built-in or custom translation style ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.translation_styles.<a href="src/soferai/translation_styles/client.py">update_translation_style</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename an owned custom style or replace its instructions. Changed instructions
are safety-validated again and invalidate translations cached under this style.
Built-in styles cannot be modified, and a custom style's target language is immutable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.translation_styles.update_translation_style(
    translation_style_id="translation_style_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**translation_style_id:** `str` — Custom translation style ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — New display name. Omit to leave unchanged.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` — Replacement style-only instructions. Omit to leave unchanged.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.translation_styles.<a href="src/soferai/translation_styles/client.py">delete_translation_style</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an owned custom translation style. Built-in styles cannot be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.translation_styles.delete_translation_style(
    translation_style_id="translation_style_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**translation_style_id:** `str` — Custom translation style ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Utils
<details><summary><code>client.utils.<a href="src/soferai/utils/client.py">get_duration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the audio duration in seconds for a provided URL or base64-encoded file.

Provide either `audio_url` or `audio_file` (base64). If both are provided, the request is invalid.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from soferai import SoferAI

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.utils.get_duration()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audio_url:** `typing.Optional[str]` — Direct URL to a downloadable audio file.
    
</dd>
</dl>

<dl>
<dd>

**audio_file:** `typing.Optional[str]` — Base64-encoded audio file content. Do not include a data URI prefix.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

