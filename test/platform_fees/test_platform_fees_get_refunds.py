from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.platform_fees import PlatformFeesClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.platform_fees.mock_data.mock_platform_fees_refund_resp import (
    mock_platform_fees_refund_resp,
)

mock_platform_fee_id = "pf_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def platform_fees_client(mock_ryft_client):
    return PlatformFeesClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_platform_fees_get_refunds(platform_fees_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_platform_fees_refund_resp()
    resp = await platform_fees_client.get_refunds(mock_platform_fee_id)
    mock_ryft_client.get.assert_called_once_with(
        f"platform-fees/{mock_platform_fee_id}/refunds"
    )
    assert resp == mock_platform_fees_refund_resp()


@pytest.mark.asyncio
async def test_platform_fees_get_refunds_error(platform_fees_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await platform_fees_client.get_refunds(mock_platform_fee_id)
