# Reference
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

**url:** `str` — URL to extract the download link from
    
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
from soferai.transcribe import TranscriptionInfo

client = SoferAI(
    api_key="YOUR_API_KEY",
)
client.transcribe.create_transcription(
    audio_url="audio_url",
    info=TranscriptionInfo(),
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

**audio_url:** `str` — URL to the audio file
    
</dd>
</dl>

<dl>
<dd>

**info:** `TranscriptionInfo` — Transcription parameters
    
</dd>
</dl>

<dl>
<dd>

**audio_id:** `typing.Optional[str]` — ID of the audio file (for audio in the S3 bucket, this is the postgres storage metadata id)
    
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

<details><summary><code>client.transcribe.<a href="src/soferai/transcribe/client.py">update_transcription_timestamps</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the timestamps based on edited text. Updates one language at a time.
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
client.transcribe.update_transcription_timestamps(
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
    language_to_update="en",
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

**language_to_update:** `Language` — Specifies which language version of the timestamps to update. Must be either 'en' for English or 'he' for Hebrew timestamps.
    
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

## Usage
<details><summary><code>client.usage.<a href="src/soferai/usage/client.py">get_usage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get usage info
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
client.usage.get_usage(
    user_id=uuid.UUID(
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

**user_id:** `uuid.UUID` — ID of the user
    
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

