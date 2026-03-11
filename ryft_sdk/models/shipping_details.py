from __future__ import annotations

from typing_extensions import NotRequired, TypedDict
from ryft_sdk.models.address import Address


class ShippingDetails(TypedDict):
    address: Address
    phoneNumber: NotRequired[str]
