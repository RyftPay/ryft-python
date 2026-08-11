from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class SellConversionRequest(TypedDict):
    currency: str
    amount: int


class BuyConversionRequest(TypedDict):
    currency: str


class CreateConversionRequest(TypedDict):
    sell: SellConversionRequest
    buy: BuyConversionRequest
    termAgreement: bool
    reason: NotRequired[str]


class GetRateRequest(TypedDict):
    buyCurrency: str
    sellCurrency: str
    amount: int


class ListConversionsRequest(TypedDict):
    limit: NotRequired[int]
    ascending: NotRequired[bool]
    startsAfter: NotRequired[str]
    startTimestamp: NotRequired[int]
    endTimestamp: NotRequired[int]
