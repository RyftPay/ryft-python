from __future__ import annotations

from typing_extensions import List, NotRequired, TypedDict


class ConversionFee(TypedDict):
    amount: int


class ConversionPlatformFeeDetail(TypedDict):
    amount: int
    ryftFee: ConversionFee


class ConversionFees(TypedDict):
    ryft: NotRequired[ConversionFee]
    platform: NotRequired[ConversionPlatformFeeDetail]


class ConversionSell(TypedDict):
    amount: int
    currency: str
    fees: NotRequired[ConversionFees]


class ConversionBuy(TypedDict):
    amount: NotRequired[int]
    currency: str
    fees: NotRequired[ConversionFees]


class ConversionCreatedBy(TypedDict):
    id: str
    name: NotRequired[str]


class Conversion(TypedDict):
    id: str
    sell: ConversionSell
    buy: ConversionBuy
    rate: NotRequired[float]
    status: str
    reason: NotRequired[str]
    estimatedSettlementDate: NotRequired[str]
    settledTimestamp: NotRequired[int]
    createdBy: NotRequired[ConversionCreatedBy]
    createdTimestamp: int


class Conversions(TypedDict):
    items: List[Conversion]
    paginationToken: NotRequired[str]


class ConversionRateSell(TypedDict):
    amount: int
    currency: str
    fees: NotRequired[ConversionFees]


class ConversionRateBuy(TypedDict):
    amount: int
    currency: str
    fees: NotRequired[ConversionFees]


class ConversionRate(TypedDict):
    sell: ConversionRateSell
    buy: ConversionRateBuy
    rate: float
    estimatedSettlementDate: NotRequired[str]
