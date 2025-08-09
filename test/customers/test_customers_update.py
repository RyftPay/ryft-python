from typing import cast
import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.customers import CustomersClient
from ryft_sdk.models.customers.req.customers_req import UpdateCustomerRequest
from ryft_sdk.models.errors import RyftError
from test.customers.mock_data import mock_update_customer_req
from test.customers.mock_data.mock_customer_resp import mock_customer_resp
from test.mock_error import mock_ryft_error
from test.customers.mock_data.mock_update_customer_req import mock_update_customer_req

mock_customer_id = "cus_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def customers_client(mock_ryft_client):
    return CustomersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_customers_update(customers_client, mock_ryft_client):
    mock_ryft_client.patch.return_value = mock_customer_resp()
    req = cast(UpdateCustomerRequest, mock_update_customer_req())
    resp = await customers_client.update(mock_customer_id, req)
    mock_ryft_client.patch.assert_called_once_with(f"customers/{mock_customer_id}", req)
    assert resp == mock_customer_resp()


@pytest.mark.asyncio
async def test_customers_update_error(customers_client, mock_ryft_client):
    mock_ryft_client.patch.side_effect = mock_ryft_error()
    req = cast(UpdateCustomerRequest, mock_update_customer_req())
    with pytest.raises(RyftError):
        await customers_client.update(mock_customer_id, req)
