import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.apple_pay import ApplePayClient
from ryft_sdk.models.errors import RyftError
from test.mock_deleted_resource_resp import mock_deleted_resource_resp
from test.mock_error import mock_ryft_error

mock_domain_id = "ap_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def apple_pay_client(mock_ryft_client):
    return ApplePayClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_apple_pay_delete_domain(apple_pay_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await apple_pay_client.delete_domain(id=mock_domain_id, account_id="acc_123")
    mock_ryft_client.delete.assert_called_once_with(
        f"apple-pay/web-domains/{mock_domain_id}", account="acc_123"
    )
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_apple_pay_register_domain_error(apple_pay_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await apple_pay_client.delete_domain(mock_domain_id, account_id="acc_123")
