from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.subscriptions import SubscriptionsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.subscriptions.req.subscriptions_req import (
    CreateSubscriptionRequest,
)
from typing import cast
from test.mock_error import mock_ryft_error
from test.subscriptions.mock_data.mock_subscriptions_create_req import (
    mock_create_subscription_req,
)
from test.subscriptions.mock_data.mock_subscriptions_resp import mock_subscription_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def subscriptions_client(mock_ryft_client):
    return SubscriptionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_subscriptions_create(subscriptions_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_subscription_resp()
    req = cast(CreateSubscriptionRequest, mock_create_subscription_req())
    resp = await subscriptions_client.create(req)
    mock_ryft_client.post.assert_called_once_with("subscriptions", req)
    assert resp == mock_subscription_resp()


@pytest.mark.asyncio
async def test_subscriptions_create_error(subscriptions_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreateSubscriptionRequest, mock_create_subscription_req())
    with pytest.raises(RyftError):
        await subscriptions_client.create(req)
