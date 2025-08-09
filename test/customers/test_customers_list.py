import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.customers import CustomersClient
from ryft_sdk.models.errors import RyftError
from test.customers.mock_data.mock_customer_resp import mock_customers_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def customers_client(mock_ryft_client):
    return CustomersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_customers_list_with_default_params(customers_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_customers_resp()
    resp = await customers_client.list()
    mock_ryft_client.get.assert_called_once_with(
        "customers",
        {
            "email": None,
            "startTimestamp": None,
            "endTimestamp": None,
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
    )
    assert resp == mock_customers_resp()


@pytest.mark.asyncio
async def test_customers_list_with_custom_params(customers_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_customers_resp()
    resp = await customers_client.list(
        email="test@ryftpay.com",
        startTimestamp=1000,
        endTimestamp=2000,
        ascending=True,
        limit=20,
        startsAfter="foo",
    )
    mock_ryft_client.get.assert_called_once_with(
        "customers",
        {
            "email": "test@ryftpay.com",
            "startTimestamp": 1000,
            "endTimestamp": 2000,
            "ascending": True,
            "limit": 20,
            "startsAfter": "foo",
        },
    )
    assert resp == mock_customers_resp()


@pytest.mark.asyncio
async def test_customers_list_error(customers_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await customers_client.list()
