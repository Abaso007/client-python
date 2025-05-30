"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from mistralai.types import BaseModel
from typing import Literal, Optional
from typing_extensions import NotRequired, TypedDict


ResponseErrorEventType = Literal["conversation.response.error"]


class ResponseErrorEventTypedDict(TypedDict):
    message: str
    code: int
    type: NotRequired[ResponseErrorEventType]
    created_at: NotRequired[datetime]


class ResponseErrorEvent(BaseModel):
    message: str

    code: int

    type: Optional[ResponseErrorEventType] = "conversation.response.error"

    created_at: Optional[datetime] = None
