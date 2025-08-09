import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.events import EventsClient
from ryft_sdk.models.errors import RyftError

from test.events.mock_data.mock_event_resp import mock_events_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def events_client(mock_ryft_client):
    return EventsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_events_list_with_defaults(events_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_events_resp()
    resp = await events_client.list(account="acc_123")
    mock_ryft_client.get.assert_called_once_with(
        "events",
        {
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
        account="acc_123",
    )
    assert resp == mock_events_resp()


@pytest.mark.asyncio
async def test_events_list_with_custom_params(events_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_events_resp()
    resp = await events_client.list(
        ascending=True, limit=20, startsAfter="foo", account="acc_123"
    )
    mock_ryft_client.get.assert_called_once_with(
        "events",
        {
            "ascending": True,
            "limit": 20,
            "startsAfter": "foo",
        },
        account="acc_123",
    )
    assert resp == mock_events_resp()


@pytest.mark.asyncio
async def test_events_get_error(events_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await events_client.list()
