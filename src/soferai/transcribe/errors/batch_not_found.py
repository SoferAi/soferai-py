# This file was auto-generated by Fern from our API Definition.

from ...core.api_error import ApiError


class BatchNotFound(ApiError):
    def __init__(self) -> None:
        super().__init__(status_code=404)
