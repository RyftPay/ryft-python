import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.webhooks import WebhooksClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.webhooks.mock_data.mock_webhooks_resp import mock_webhooks_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def webhooks_client(mock_ryft_client):
    return WebhooksClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_webhooks_list(webhooks_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_webhooks_resp()
    resp = await webhooks_client.list()
    mock_ryft_client.get.assert_called_once_with("webhooks")
    assert resp == mock_webhooks_resp()


@pytest.mark.asyncio
async def test_webhooks_list_error(webhooks_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await webhooks_client.list()
