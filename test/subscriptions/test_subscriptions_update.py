from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.subscriptions import SubscriptionsClient
from ryft_sdk.models.errors import RyftError
from typing import cast
from ryft_sdk.models.subscriptions.req.subscriptions_req import (
    UpdateSubscriptionRequest,
)
from test.mock_error import mock_ryft_error
from test.subscriptions.mock_data.mock_subscriptions_resp import mock_subscription_resp
from test.subscriptions.mock_data.mock_subscriptions_update_req import (
    mock_update_subscription_req,
)

mock_subscription_id = "sub_1234567890"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def subscriptions_client(mock_ryft_client):
    return SubscriptionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_subscriptions_update(subscriptions_client, mock_ryft_client):
    mock_ryft_client.patch.return_value = mock_subscription_resp()
    req = cast(UpdateSubscriptionRequest, mock_update_subscription_req())
    resp = await subscriptions_client.update(mock_subscription_id, req)
    mock_ryft_client.patch.assert_called_once_with(
        f"subscriptions/{mock_subscription_id}", req
    )
    assert resp == mock_subscription_resp()


@pytest.mark.asyncio
async def test_subscriptions_update_error(subscriptions_client, mock_ryft_client):
    mock_ryft_client.patch.side_effect = mock_ryft_error()
    req = cast(UpdateSubscriptionRequest, mock_update_subscription_req())
    with pytest.raises(RyftError):
        await subscriptions_client.update(mock_subscription_id, req)
