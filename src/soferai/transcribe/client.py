# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .types.transcription_info import TranscriptionInfo
from ..core.request_options import RequestOptions
from .types.transcription_id import TranscriptionId
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from .errors.authentication_error import AuthenticationError
from .errors.rate_limit_error import RateLimitError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
import uuid
from ..core.jsonable_encoder import jsonable_encoder
from .errors.transcription_not_found import TranscriptionNotFound
from .types.transcription import Transcription
from .types.timestamp import Timestamp
from .types.language import Language
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TranscribeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_transcription(
        self,
        *,
        audio_url: str,
        info: TranscriptionInfo,
        audio_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptionId:
        """
        Create a new transcription

        Parameters
        ----------
        audio_url : str
            URL to the audio file

        info : TranscriptionInfo
            Transcription parameters

        audio_id : typing.Optional[str]
            ID of the audio file (for audio in the S3 bucket, this is the postgres storage metadata id)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionId

        Examples
        --------
        from soferai import SoferAI
        from soferai.transcribe import TranscriptionInfo

        client = SoferAI(
            api_key="YOUR_API_KEY",
        )
        client.transcribe.create_transcription(
            audio_url="audio_url",
            info=TranscriptionInfo(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/transcriptions/",
            method="POST",
            json={
                "audio_url": audio_url,
                "audio_id": audio_id,
                "info": convert_and_respect_annotation_metadata(
                    object_=info, annotation=TranscriptionInfo, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TranscriptionId,
                    parse_obj_as(
                        type_=TranscriptionId,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_transcription_status(
        self, transcription_id: uuid.UUID, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TranscriptionInfo:
        """
        Get transcription status

        Parameters
        ----------
        transcription_id : uuid.UUID
            ID of the transcription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionInfo

        Examples
        --------
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
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/transcriptions/{jsonable_encoder(transcription_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TranscriptionInfo,
                    parse_obj_as(
                        type_=TranscriptionInfo,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise TranscriptionNotFound()
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_transcription(
        self, transcription_id: uuid.UUID, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Transcription:
        """
        Get transcription

        Parameters
        ----------
        transcription_id : uuid.UUID
            ID of the transcription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcription

        Examples
        --------
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
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/transcriptions/{jsonable_encoder(transcription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Transcription,
                    parse_obj_as(
                        type_=Transcription,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise TranscriptionNotFound()
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_transcription_timestamps(
        self,
        *,
        old_timestamps: typing.Sequence[Timestamp],
        edited_text: str,
        language_to_update: Language,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Timestamp]:
        """
        Update the timestamps based on edited text. Updates one language at a time.

        Parameters
        ----------
        old_timestamps : typing.Sequence[Timestamp]
            The original timestamps associated with the text before editing. These will be used as reference points to align the new timestamps.

        edited_text : str
            The modified version of the transcription text that needs updated timestamp alignments. This should be the complete text after your edits.

        language_to_update : Language
            Specifies which language version of the timestamps to update. Must be either 'en' for English or 'he' for Hebrew timestamps.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Timestamp]

        Examples
        --------
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
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/transcriptions/update-timestamps",
            method="POST",
            json={
                "old_timestamps": convert_and_respect_annotation_metadata(
                    object_=old_timestamps, annotation=typing.Sequence[Timestamp], direction="write"
                ),
                "edited_text": edited_text,
                "language_to_update": language_to_update,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Timestamp],
                    parse_obj_as(
                        type_=typing.List[Timestamp],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise TranscriptionNotFound()
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTranscribeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_transcription(
        self,
        *,
        audio_url: str,
        info: TranscriptionInfo,
        audio_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranscriptionId:
        """
        Create a new transcription

        Parameters
        ----------
        audio_url : str
            URL to the audio file

        info : TranscriptionInfo
            Transcription parameters

        audio_id : typing.Optional[str]
            ID of the audio file (for audio in the S3 bucket, this is the postgres storage metadata id)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionId

        Examples
        --------
        import asyncio

        from soferai import AsyncSoferAI
        from soferai.transcribe import TranscriptionInfo

        client = AsyncSoferAI(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcribe.create_transcription(
                audio_url="audio_url",
                info=TranscriptionInfo(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/transcriptions/",
            method="POST",
            json={
                "audio_url": audio_url,
                "audio_id": audio_id,
                "info": convert_and_respect_annotation_metadata(
                    object_=info, annotation=TranscriptionInfo, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TranscriptionId,
                    parse_obj_as(
                        type_=TranscriptionId,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_transcription_status(
        self, transcription_id: uuid.UUID, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TranscriptionInfo:
        """
        Get transcription status

        Parameters
        ----------
        transcription_id : uuid.UUID
            ID of the transcription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranscriptionInfo

        Examples
        --------
        import asyncio
        import uuid

        from soferai import AsyncSoferAI

        client = AsyncSoferAI(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcribe.get_transcription_status(
                transcription_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/transcriptions/{jsonable_encoder(transcription_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TranscriptionInfo,
                    parse_obj_as(
                        type_=TranscriptionInfo,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise TranscriptionNotFound()
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_transcription(
        self, transcription_id: uuid.UUID, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Transcription:
        """
        Get transcription

        Parameters
        ----------
        transcription_id : uuid.UUID
            ID of the transcription

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transcription

        Examples
        --------
        import asyncio
        import uuid

        from soferai import AsyncSoferAI

        client = AsyncSoferAI(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcribe.get_transcription(
                transcription_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/transcriptions/{jsonable_encoder(transcription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Transcription,
                    parse_obj_as(
                        type_=Transcription,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise TranscriptionNotFound()
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_transcription_timestamps(
        self,
        *,
        old_timestamps: typing.Sequence[Timestamp],
        edited_text: str,
        language_to_update: Language,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Timestamp]:
        """
        Update the timestamps based on edited text. Updates one language at a time.

        Parameters
        ----------
        old_timestamps : typing.Sequence[Timestamp]
            The original timestamps associated with the text before editing. These will be used as reference points to align the new timestamps.

        edited_text : str
            The modified version of the transcription text that needs updated timestamp alignments. This should be the complete text after your edits.

        language_to_update : Language
            Specifies which language version of the timestamps to update. Must be either 'en' for English or 'he' for Hebrew timestamps.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Timestamp]

        Examples
        --------
        import asyncio

        from soferai import AsyncSoferAI
        from soferai.transcribe import Timestamp

        client = AsyncSoferAI(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.transcribe.update_transcription_timestamps(
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


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/transcriptions/update-timestamps",
            method="POST",
            json={
                "old_timestamps": convert_and_respect_annotation_metadata(
                    object_=old_timestamps, annotation=typing.Sequence[Timestamp], direction="write"
                ),
                "edited_text": edited_text,
                "language_to_update": language_to_update,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Timestamp],
                    parse_obj_as(
                        type_=typing.List[Timestamp],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise TranscriptionNotFound()
            if _response.status_code == 401:
                raise AuthenticationError()
            if _response.status_code == 429:
                raise RateLimitError()
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
