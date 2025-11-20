from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.webhooks import WebhooksClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.webhooks.mock_data.mock_webhooks_resp import mock_webhook_resp

mock_webhook_id = "wg_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def webhooks_client(mock_ryft_client):
    return WebhooksClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_webhooks_get(webhooks_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_webhook_resp()
    resp = await webhooks_client.get(mock_webhook_id)
    mock_ryft_client.get.assert_called_once_with(f"webhooks/{mock_webhook_id}")
    assert resp == mock_webhook_resp()


@pytest.mark.asyncio
async def test_webhooks_get_error(webhooks_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await webhooks_client.get(mock_webhook_id)
