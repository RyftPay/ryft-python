import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.subscriptions import SubscriptionsClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.subscriptions.mock_data.mock_subscriptions_resp import (
    mock_payment_sessions_resp,
)

mock_subscription_id = "sub_1234567890"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def subscriptions_client(mock_ryft_client):
    return SubscriptionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_subscriptions_get_payment_sessions_with_default_params(
    subscriptions_client, mock_ryft_client
):
    mock_ryft_client.get.return_value = mock_payment_sessions_resp()
    resp = await subscriptions_client.get_payment_sessions(mock_subscription_id)
    mock_ryft_client.get.assert_called_once_with(
        f"subscriptions/{mock_subscription_id}/payment-sessions",
        {
            "startTimestamp": None,
            "endTimestamp": None,
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
    )
    assert resp == mock_payment_sessions_resp()


@pytest.mark.asyncio
async def test_subscriptions_get_payment_sessions_with_custom_params(
    subscriptions_client, mock_ryft_client
):
    mock_ryft_client.get.return_value = mock_payment_sessions_resp()
    resp = await subscriptions_client.get_payment_sessions(
        mock_subscription_id,
        startTimestamp=1234567890,
        endTimestamp=1234567891,
        ascending=True,
        limit=10,
        startsAfter="abc",
    )
    mock_ryft_client.get.assert_called_once_with(
        f"subscriptions/{mock_subscription_id}/payment-sessions",
        {
            "startTimestamp": 1234567890,
            "endTimestamp": 1234567891,
            "ascending": True,
            "limit": 10,
            "startsAfter": "abc",
        },
    )
    assert resp == mock_payment_sessions_resp()


@pytest.mark.asyncio
async def test_subscriptions_get_payment_sessions_error(
    subscriptions_client, mock_ryft_client
):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await subscriptions_client.get_payment_sessions(mock_subscription_id)
