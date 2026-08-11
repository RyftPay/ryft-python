from __future__ import annotations

import pytest
from unittest.mock import Mock
from typing import cast
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.conversions import ConversionsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.conversions.req.conversions_req import GetRateRequest
from test.mock_error import mock_ryft_error
from test.conversions.mock_data.mock_conversions_resp import mock_conversion_rate_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def conversions_client(mock_ryft_client):
    return ConversionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_conversions_get_rate_with_defaults(conversions_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_conversion_rate_resp()
    resp = await conversions_client.get_rate()
    mock_ryft_client.get.assert_called_once_with("conversions/rate", None)
    assert resp == mock_conversion_rate_resp()


@pytest.mark.asyncio
async def test_conversions_get_rate_with_custom_params(
    conversions_client, mock_ryft_client
):
    mock_ryft_client.get.return_value = mock_conversion_rate_resp()
    req = cast(
        GetRateRequest,
        {"buyCurrency": "EUR", "sellCurrency": "GBP", "amount": 1000},
    )
    resp = await conversions_client.get_rate(req)
    mock_ryft_client.get.assert_called_once_with("conversions/rate", req)
    assert resp == mock_conversion_rate_resp()


@pytest.mark.asyncio
async def test_conversions_get_rate_error(conversions_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await conversions_client.get_rate()
