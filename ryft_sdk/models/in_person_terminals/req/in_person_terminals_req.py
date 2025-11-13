from typing import Any, Optional, TypedDict


class CreateTerminalRequest(TypedDict):
    serialNumber: str
    name: Optional[str]
    locationId: Optional[str]
    metadata: Optional[dict[str, str]]


class UpdateTerminalRequest(TypedDict):
    locationId: Optional[str]
    name: Optional[str]
    metadata: Optional[dict[str, str]]


class TerminalPaymentRequest(TypedDict):
    amounts: dict[str, Any]
    receiptPrintingSource: Optional[str]
    skipCustomerReceipt: Optional[bool]
    skipMerchantReceipt: Optional[bool]
    metadata: Optional[dict[str, str]]


class TerminalRefundRequest(TypedDict):
    paymentSession: dict[str, str]
    amounts: dict[str, Any]
    receiptPrintingSource: Optional[str]
    skipCustomerReceipt: Optional[bool]
    skipMerchantReceipt: Optional[bool]
    metadata: Optional[dict[str, str]]


class TerminalConfirmReceiptRequest(TypedDict):
    customerReceiptStatus: Optional[str]
    merchantReceiptStatus: Optional[str]
