import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_methods import PaymentMethodsClient
from ryft_sdk.models.errors import RyftError
from test.mock_deleted_resource_resp import mock_deleted_resource_resp
from test.mock_error import mock_ryft_error

mock_payment_method_id = "pm_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payment_methods_client(mock_ryft_client):
    return PaymentMethodsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payment_methods_delete(payment_methods_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await payment_methods_client.delete(mock_payment_method_id)
    mock_ryft_client.delete.assert_called_once_with(
        f"payment-methods/{mock_payment_method_id}"
    )
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_payment_methods_delete_error(payment_methods_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await payment_methods_client.delete(mock_payment_method_id)
