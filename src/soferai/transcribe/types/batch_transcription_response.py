# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import uuid
import pydantic
import typing
from .transcription_id import TranscriptionId
from .batch_status import BatchStatus


class BatchTranscriptionResponse(UniversalBaseModel):
    batch_id: uuid.UUID = pydantic.Field()
    """
    Unique identifier for the batch
    """

    transcription_ids: typing.List[TranscriptionId] = pydantic.Field()
    """
    List of transcription IDs that were created for this batch
    """

    total_count: int = pydantic.Field()
    """
    Total number of transcriptions in the batch
    """

    status: BatchStatus = pydantic.Field()
    """
    Current status of the batch
    """

    model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
