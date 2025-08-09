import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.webhooks import WebhooksClient
from ryft_sdk.models.errors import RyftError
from test.mock_deleted_resource_resp import mock_deleted_resource_resp
from test.mock_error import mock_ryft_error

mock_webhook_id = "wh_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def webhooks_client(mock_ryft_client):
    return WebhooksClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_webhooks_delete(webhooks_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await webhooks_client.delete(mock_webhook_id)
    mock_ryft_client.delete.assert_called_once_with(f"webhooks/{mock_webhook_id}", {})
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_webhooks_delete_error(webhooks_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await webhooks_client.delete(mock_webhook_id)
