from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.webhooks import WebhooksClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.webhooks.req.webhooks_req import CreateWebhookRequest
from typing import cast
from test.mock_error import mock_ryft_error
from test.webhooks.mock_data.mock_webhooks_create_req import mock_create_webhook_req
from test.webhooks.mock_data.mock_webhooks_resp import mock_webhook_created_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def webhooks_client(mock_ryft_client):
    return WebhooksClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_webhooks_create(webhooks_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_webhook_created_resp()
    req = cast(CreateWebhookRequest, mock_create_webhook_req())
    resp = await webhooks_client.create(req)
    mock_ryft_client.post.assert_called_once_with("webhooks", req)
    assert resp == mock_webhook_created_resp()


@pytest.mark.asyncio
async def test_webhooks_create_error(webhooks_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreateWebhookRequest, mock_create_webhook_req())
    with pytest.raises(RyftError):
        await webhooks_client.create(req)
