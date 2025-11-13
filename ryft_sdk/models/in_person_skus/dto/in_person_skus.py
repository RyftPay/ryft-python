from typing import List, Optional, TypedDict


class InPersonProductSku(TypedDict):
    id: str
    name: str
    country: str
    totalAmount: int
    currency: str
    status: str
    productId: str
    createdTimestamp: int
    lastUpdatedTimestamp: int


class InPersonProductSkus(TypedDict):
    items: List[InPersonProductSku]
    paginationToken: Optional[str]
