from __future__ import annotations

from typing import cast, Optional
from ryft_sdk.client import RyftClient
from ryft_sdk.models.conversions.dto.conversions import Conversion, Conversions, ConversionRate
from ryft_sdk.models.conversions.req.conversions_req import (
    CreateConversionRequest,
    GetRateRequest,
    ListConversionsRequest,
)


class ConversionsClient:
    def __init__(self, client: RyftClient):
        self.client = client
        self.path = "conversions"

    async def create(self, req: CreateConversionRequest) -> Conversion:
        return cast(Conversion, self.client.post(self.path, cast(dict, req)))

    async def get(self, id: str) -> Conversion:
        return cast(Conversion, self.client.get(f"{self.path}/{id}"))

    async def list(self, req: Optional[ListConversionsRequest] = None) -> Conversions:
        return cast(
            Conversions,
            self.client.get(self.path, cast(dict, req) if req else None),
        )

    async def get_rate(self, req: Optional[GetRateRequest] = None) -> ConversionRate:
        return cast(
            ConversionRate,
            self.client.get(f"{self.path}/rate", cast(dict, req) if req else None),
        )
