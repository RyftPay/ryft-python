import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.apple_pay import ApplePayClient
from ryft_sdk.models.errors import RyftError
from test.apple_pay.mock_data.mock_apple_pay_domain_resp import (
    mock_apple_pay_domain_resp,
)
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def apple_pay_client(mock_ryft_client):
    return ApplePayClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_apple_pay_register_domain(apple_pay_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_apple_pay_domain_resp()
    resp = await apple_pay_client.register_domain(
        domain="example.com", account_id="acc_123"
    )
    mock_ryft_client.post.assert_called_once_with(
        "apple-pay/web-domains", {"domainName": "example.com"}, "acc_123"
    )
    assert resp == mock_apple_pay_domain_resp()


@pytest.mark.asyncio
async def test_apple_pay_register_domain_error(apple_pay_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await apple_pay_client.register_domain("example.com", account_id="acc_123")
