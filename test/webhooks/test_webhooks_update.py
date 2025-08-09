import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.webhooks import WebhooksClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.webhooks.req.webhooks_req import UpdateWebhookRequest
from typing import cast
from test.mock_error import mock_ryft_error
from test.webhooks.mock_data.mock_webhooks_resp import mock_webhook_resp
from test.webhooks.mock_data.mock_webhooks_update_req import mock_update_webhook_req

mock_webhook_id = "wh_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def webhooks_client(mock_ryft_client):
    return WebhooksClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_webhooks_update(webhooks_client, mock_ryft_client):
    mock_ryft_client.patch.return_value = mock_webhook_resp()
    req = cast(UpdateWebhookRequest, mock_update_webhook_req())
    resp = await webhooks_client.update(mock_webhook_id, req)
    mock_ryft_client.patch.assert_called_once_with(f"webhooks/{mock_webhook_id}", req)
    assert resp == mock_webhook_resp()


@pytest.mark.asyncio
async def test_webhooks_update_error(webhooks_client, mock_ryft_client):
    mock_ryft_client.patch.side_effect = mock_ryft_error()
    req = cast(UpdateWebhookRequest, mock_update_webhook_req())
    with pytest.raises(RyftError):
        await webhooks_client.update(mock_webhook_id, req)
