"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai.types import BaseModel
import pydantic
from typing import Final, Literal, Optional, TypedDict
from typing_extensions import Annotated


TextChunkType = Literal["text"]


class TextChunkTypedDict(TypedDict):
    text: str


class TextChunk(BaseModel):
    text: str

    # fmt: off
    TYPE: Annotated[Final[Optional[TextChunkType]], pydantic.Field(alias="type")] = "text" # type: ignore
    # fmt: on
