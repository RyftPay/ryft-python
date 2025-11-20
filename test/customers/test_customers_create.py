from __future__ import annotations

from typing import cast
import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.customers import CustomersClient
from ryft_sdk.models.customers.req.customers_req import CreateCustomerRequest
from ryft_sdk.models.errors import RyftError
from test.customers.mock_data.mock_create_customer_req import mock_create_customer_req
from test.customers.mock_data.mock_customer_resp import mock_customer_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def customers_client(mock_ryft_client):
    return CustomersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_customers_create(customers_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_customer_resp()
    req = cast(CreateCustomerRequest, mock_create_customer_req())
    resp = await customers_client.create(req)
    mock_ryft_client.post.assert_called_once_with("customers", req)
    assert resp == mock_customer_resp()


@pytest.mark.asyncio
async def test_customers_create_error(customers_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreateCustomerRequest, mock_create_customer_req())
    with pytest.raises(RyftError):
        await customers_client.create(req)
