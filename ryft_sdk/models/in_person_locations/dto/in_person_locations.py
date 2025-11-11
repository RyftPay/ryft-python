from typing import Any, List, Optional, TypedDict


class InPersonLocation(TypedDict, total=False):
    id: str
    name: str
    address: dict[str, Any]
    geoCoordinates: Optional[dict[str, Any]]
    metadata: Optional[dict[str, str]]
    createdTimestamp: int
    lastUpdatedTimestamp: int


class InPersonLocationDeleted(TypedDict, total=False):
    id: str


class InPersonLocations(TypedDict, total=False):
    items: List[InPersonLocation]
    paginationToken: Optional[str]
