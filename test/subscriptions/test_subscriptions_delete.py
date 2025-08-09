import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.subscriptions import SubscriptionsClient
from ryft_sdk.models.errors import RyftError
from test.mock_deleted_resource_resp import mock_deleted_resource_resp
from test.mock_error import mock_ryft_error

mock_subscription_id = "sub_1234567890"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def subscriptions_client(mock_ryft_client):
    return SubscriptionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_subscriptions_delete(subscriptions_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await subscriptions_client.delete(mock_subscription_id)
    mock_ryft_client.delete.assert_called_once_with(
        f"subscriptions/{mock_subscription_id}", {}
    )
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_subscriptions_delete_error(subscriptions_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await subscriptions_client.delete(mock_subscription_id)
