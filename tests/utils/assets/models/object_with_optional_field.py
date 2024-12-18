# This file was auto-generated by Fern from our API Definition.

# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing
import typing_extensions
from SoferAi.core.serialization import FieldMetadata
import datetime as dt
import uuid
from .color import Color
from .shape import ShapeParams
from .undiscriminated_shape import UndiscriminatedShapeParams


class ObjectWithOptionalFieldParams(typing_extensions.TypedDict):
    literal: typing.Literal["lit_one"]
    string: typing_extensions.NotRequired[str]
    integer: typing_extensions.NotRequired[int]
    long_: typing_extensions.NotRequired[typing_extensions.Annotated[int, FieldMetadata(alias="long")]]
    double: typing_extensions.NotRequired[float]
    bool_: typing_extensions.NotRequired[typing_extensions.Annotated[bool, FieldMetadata(alias="bool")]]
    datetime: typing_extensions.NotRequired[dt.datetime]
    date: typing_extensions.NotRequired[dt.date]
    uuid_: typing_extensions.NotRequired[typing_extensions.Annotated[uuid.UUID, FieldMetadata(alias="uuid")]]
    base_64: typing_extensions.NotRequired[typing_extensions.Annotated[str, FieldMetadata(alias="base64")]]
    list_: typing_extensions.NotRequired[typing_extensions.Annotated[typing.Sequence[str], FieldMetadata(alias="list")]]
    set_: typing_extensions.NotRequired[typing_extensions.Annotated[typing.Set[str], FieldMetadata(alias="set")]]
    map_: typing_extensions.NotRequired[typing_extensions.Annotated[typing.Dict[int, str], FieldMetadata(alias="map")]]
    enum: typing_extensions.NotRequired[Color]
    union: typing_extensions.NotRequired[ShapeParams]
    second_union: typing_extensions.NotRequired[ShapeParams]
    undiscriminated_union: typing_extensions.NotRequired[UndiscriminatedShapeParams]
    any: typing.Optional[typing.Any]
