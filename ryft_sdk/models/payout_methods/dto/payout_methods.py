from __future__ import annotations

from typing_extensions import List, NotRequired, TypedDict
from ryft_sdk.models.address import Address


class BankAccount(TypedDict):
    bankIdType: str
    bankId: NotRequired[str]
    accountNumberType: str
    accountNumber: str
    address: NotRequired[Address]


class PayoutMethodVerification(TypedDict):
    status: str
    nameOnAccount: NotRequired[str]
    rejectionReason: NotRequired[str]


class PayoutMethod(TypedDict):
    id: str
    type: str
    displayName: NotRequired[str]
    status: str
    invalidReason: NotRequired[str]
    currency: str
    countryCode: str
    bankAccount: BankAccount
    createdTimestamp: int
    lastUpdatedTimestamp: int
    verification: PayoutMethodVerification


class PayoutMethods(TypedDict):
    items: List[PayoutMethod]
    paginationToken: NotRequired[str]
