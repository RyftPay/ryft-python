from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.clients.apple_pay import ApplePayClient
from test.apple_pay.mock_data import mock_apple_pay_domain_resp
from test.apple_pay.mock_data.mock_apple_pay_domain_resp import (
    mock_apple_pay_domain_resp,
)
from test.mock_error import mock_ryft_error

mock_account_id = "acc_123"
mock_domain_id = "ap_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def apple_pay_client(mock_ryft_client):
    return ApplePayClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_apple_pay_get_domain(apple_pay_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_apple_pay_domain_resp()
    resp = await apple_pay_client.get_domain(
        id=mock_domain_id, account_id=mock_account_id
    )
    mock_ryft_client.get.assert_called_once_with(
        f"apple-pay/web-domains/{mock_domain_id}",
        {},
        mock_account_id,
    )
    assert resp == mock_apple_pay_domain_resp()


@pytest.mark.asyncio
async def test_apple_pay_get_domain_error(apple_pay_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await apple_pay_client.get_domain(id=mock_domain_id)
