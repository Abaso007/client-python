"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .chatcompletionchoice import ChatCompletionChoice, ChatCompletionChoiceTypedDict
from .usageinfo import UsageInfo, UsageInfoTypedDict
from mistralai.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ChatCompletionResponseTypedDict(TypedDict):
    id: str
    object: str
    model: str
    usage: UsageInfoTypedDict
    created: int
    choices: List[ChatCompletionChoiceTypedDict]


class ChatCompletionResponse(BaseModel):
    id: str

    object: str

    model: str

    usage: UsageInfo

    created: int

    choices: List[ChatCompletionChoice]
