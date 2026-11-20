from __future__ import annotations

from typing_extensions import List, NotRequired, TypedDict


class PayoutBankAccount(TypedDict):
    bankIdType: NotRequired[str]
    bankId: NotRequired[str]
    bankName: NotRequired[str]
    accountNumberType: str
    last4: str


class PayoutMethod(TypedDict):
    id: str
    bankAccount: PayoutBankAccount


class FailureDetail(TypedDict):
    # invalid_payout_method, invalid_account_address or unknown_error. New codes may be added.
    code: str
    description: str


class Payout(TypedDict):
    id: str
    paymentsTakeDateFrom: str
    paymentsTakeDateTo: str
    amount: int
    currency: str
    status: str
    scheduleType: str
    payoutMethod: NotRequired[PayoutMethod]
    # Deprecated: use failureDetail, which gives the specific reason the payout failed
    failureReason: NotRequired[str]
    failureDetail: NotRequired[FailureDetail]
    scheme: NotRequired[str]
    createdTimestamp: int
    scheduledTimestamp: int
    completedTimestamp: NotRequired[int]
    metadata: NotRequired[dict[str, str]]


class Payouts(TypedDict):
    payouts: List[Payout]
    paginationToken: NotRequired[str]
