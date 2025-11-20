from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.customers import CustomersClient
from ryft_sdk.models.errors import RyftError
from test.customers.mock_data.mock_customer_resp import mock_customer_resp
from test.mock_error import mock_ryft_error

mock_customer_id = "cus_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def customers_client(mock_ryft_client):
    return CustomersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_customers_get(customers_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_customer_resp()
    resp = await customers_client.get(mock_customer_id)
    mock_ryft_client.get.assert_called_once_with(f"customers/{mock_customer_id}")
    assert resp == mock_customer_resp()


@pytest.mark.asyncio
async def test_customers_get_error(customers_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await customers_client.get(mock_customer_id)
