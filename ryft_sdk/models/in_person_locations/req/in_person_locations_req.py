from typing import Any, Optional, TypedDict


class CreateInPersonLocationRequest(TypedDict):
    name: str
    address: dict[str, Any]
    geoCoordinates: Optional[dict[str, Any]]
    metadata: Optional[dict[str, str]]


class UpdateInPersonLocationRequest(TypedDict):
    name: Optional[str]
    metadata: Optional[dict[str, str]]
