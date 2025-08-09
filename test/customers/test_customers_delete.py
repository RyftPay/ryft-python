import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.customers import CustomersClient
from ryft_sdk.models.errors import RyftError
from test.mock_deleted_resource_resp import mock_deleted_resource_resp
from test.mock_error import mock_ryft_error

mock_customer_id = "cus_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def customers_client(mock_ryft_client):
    return CustomersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_customers_delete(customers_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await customers_client.delete(mock_customer_id)
    mock_ryft_client.delete.assert_called_once_with(f"customers/{mock_customer_id}", {})
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_customers_delete_error(customers_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await customers_client.delete(mock_customer_id)
