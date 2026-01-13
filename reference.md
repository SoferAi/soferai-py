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

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">create_batch_transcription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple transcriptions in a single batch request.

**Choose a processing mode:**

- **Express mode**: Transcriptions start immediately. Max 10 files. Higher cost. Pass `audio_sources` directly in the request.
- **Standard mode**: Transcriptions processed within 24 hours. Max 500 files. Lower cost. First upload a manifest via [Upload Batch File](/api-reference/transcribe/upload-batch-file), then pass the `batch_file_id` here.

All files in the batch share the same transcription settings (model, language, etc.) defined in `info`.
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
from soferai.transcribe import TranscriptionRequestInfo

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.transcribe.create_batch_transcription(
    batch_file_id=uuid.UUID(
        "f1234567-89ab-cdef-0123-456789abcdef",
    ),
    info=TranscriptionRequestInfo(
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

**info:** `TranscriptionRequestInfo` — Transcription settings applied to all files in the batch (model, language, etc.)
    
</dd>
</dl>

<dl>
<dd>

**processing_mode:** `typing.Optional[ProcessingMode]` 

Choose how the batch is processed:
- `standard` (default): Lower cost, processed within 24 hours. Max 500 files. Use with `batch_file_id`.
- `express`: Higher cost, starts immediately. Max 10 files. Use with `audio_sources`.
    
</dd>
</dl>

<dl>
<dd>

**batch_file_id:** `typing.Optional[uuid.UUID]` 

**For standard mode only.** ID of a previously uploaded batch manifest.

Get this by calling [Upload Batch File](/api-reference/transcribe/upload-batch-file) first.
    
</dd>
</dl>

<dl>
<dd>

**audio_sources:** `typing.Optional[typing.Sequence[BatchAudioSource]]` 

**For express mode only.** List of audio URLs to transcribe (max 10).

Each item needs an `audio_url` and can optionally include a `title`.
    
</dd>
</dl>

<dl>
<dd>

**batch_title:** `typing.Optional[str]` — Default title prefix for transcriptions. Individual items can override this. Items without titles become "{batch_title} - Item 1", "{batch_title} - Item 2", etc.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[uuid.UUID]` — Custom UUID for this batch. Auto-generated if not provided.
    
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

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">upload_batch_file</a>(...)</code></summary>
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
2. Use that ID in [Create Batch Transcription](/api-reference/transcribe/create-batch-transcription) with `processing_mode: "standard"`

The manifest is a list of audio sources (max 500), each with a URL and optional title. You can provide it as a JSON array or JSONL format.
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
client.transcribe.upload_batch_file(
    content_type="jsonl",
    jsonl='{"audio_url": "https://example.com/shiur1.mp3", "title": "Shiur 1"}\n{"audio_url": "https://example.com/shiur2.mp3", "title": "Shiur 2"}',
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

**json_items:** `typing.Optional[typing.Sequence[BatchAudioSource]]` — **For JSON format.** Array of audio sources to transcribe (max 500).
    
</dd>
</dl>

<dl>
<dd>

**jsonl:** `typing.Optional[str]` 

**For JSONL format.** One audio source per line as JSON, separated by newlines (max 500 lines).

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

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">list_batch_files</a>()</code></summary>
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
client.transcribe.list_batch_files()

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

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">get_batch_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a specific batch file manifest, including its validation status. Check this after uploading to ensure your manifest is valid before starting a batch.
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
client.transcribe.get_batch_file(
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

**batch_file_id:** `uuid.UUID` — The batch file ID returned from [Upload Batch File](/api-reference/transcribe/upload-batch-file)
    
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

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">get_batch_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the progress of a batch transcription. Returns counts of completed, failed, and pending transcriptions, plus details for each individual transcription.
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
client.transcribe.get_batch_status(
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

**batch_id:** `uuid.UUID` — The batch ID returned from [Create Batch Transcription](/api-reference/transcribe/create-batch-transcription)
    
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

**filter_hebrew_word_format:** `typing.Optional[str]` — Optionally filter the response to a single Hebrew word format. If set to 'en', the response text will have Hebrew characters removed and timestamps will exclude words tagged with 'he'. If set to 'he', italicized transliterations are removed from the text and timestamps will exclude words tagged only with 'en'. If set to 'hybrid', the response includes both transliteration and Hebrew characters for each word.
    
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

## Transformations
<details><summary><code>client.transformations.<a href="src/soferai/transformations/client.py">generate_summary</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a Markdown summary for a transcription. If a summary already exists, it is returned.
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
client.transformations.generate_summary(
    transcription_id_=uuid.UUID(
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

**transcription_id_:** `uuid.UUID` — ID of the transcription to summarize
    
</dd>
</dl>

<dl>
<dd>

**transcription_id:** `uuid.UUID` — ID of the transcription to summarize
    
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

<details><summary><code>client.transformations.<a href="src/soferai/transformations/client.py">get_summary</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the Markdown summary for a transcription if it exists.
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
client.transformations.get_summary(
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

**transcription_id:** `uuid.UUID` — ID of the transcription to fetch summary for
    
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

