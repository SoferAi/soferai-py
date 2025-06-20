# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing


class LinkResponse(UniversalBaseModel):
    title: str = pydantic.Field()
    """
    Title of the file
    """

    download_url: str = pydantic.Field()
    """
    Download URL of the file
    """

    file_format: str = pydantic.Field()
    """
    Format of the file
    """

    file_name: str = pydantic.Field()
    """
    Name of the file
    """

    model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
