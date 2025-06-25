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

Get account balance in cents
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

Create multiple transcriptions to be processed in batch
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
from soferai.transcribe import AudioSource, TranscriptionRequestInfo

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.transcribe.create_batch_transcription(
    audio_sources=[AudioSource(), AudioSource()],
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

**audio_sources:** `typing.Sequence[AudioSource]` — List of audio sources to transcribe with the same settings. Each item should have either audio_url or audio_file.
    
</dd>
</dl>

<dl>
<dd>

**info:** `TranscriptionRequestInfo` — Shared transcription parameters for all audio files in the batch
    
</dd>
</dl>

<dl>
<dd>

**batch_title:** `typing.Optional[str]` — Optional title for the batch. The system will first check for a title in the Audio Source itself. If no title is provided there, it defaults to batch title providded here with "- Batch Item N" appended.
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[uuid.UUID]` — Optional ID for the batch. If not provided, a UUID will be generated.
    
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

Get status of a batch transcription
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

**batch_id:** `uuid.UUID` — ID of the batch. Use the ID returned from the Create Batch Transcription endpoint.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

