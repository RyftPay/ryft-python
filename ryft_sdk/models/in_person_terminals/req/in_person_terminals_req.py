from typing import Any, Optional, TypedDict


class CreateTerminalRequest(TypedDict, total=False):
    serialNumber: str
    name: Optional[str]
    locationId: Optional[str]
    metadata: Optional[dict[str, str]]


class UpdateTerminalRequest(TypedDict, total=False):
    locationId: Optional[str]
    name: Optional[str]
    metadata: Optional[dict[str, str]]


class TerminalPaymentRequest(TypedDict, total=False):
    amounts: dict[str, Any]
    receiptPrintingSource: Optional[str]
    skipCustomerReceipt: Optional[bool]
    skipMerchantReceipt: Optional[bool]
    metadata: Optional[dict[str, str]]


class TerminalRefundRequest(TypedDict, total=False):
    paymentSession: dict[str, str]
    amounts: dict[str, Any]
    receiptPrintingSource: Optional[str]
    skipCustomerReceipt: Optional[bool]
    skipMerchantReceipt: Optional[bool]
    metadata: Optional[dict[str, str]]


class TerminalConfirmReceiptRequest(TypedDict, total=False):
    customerReceiptStatus: Optional[str]
    merchantReceiptStatus: Optional[str]
