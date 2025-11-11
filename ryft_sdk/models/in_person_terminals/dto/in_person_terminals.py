from typing import Any, List, Optional, TypedDict


class Terminal(TypedDict, total=False):
    id: str
    name: str
    location: dict[str, str]
    device: dict[str, Any]
    action: Optional[dict[str, Any]]
    metadata: Optional[dict[str, str]]
    createdTimestamp: int
    lastUpdatedTimestamp: int


class TerminalDeleted(TypedDict, total=False):
    id: str


class Terminals(TypedDict, total=False):
    items: List[Terminal]
    paginationToken: Optional[str]
