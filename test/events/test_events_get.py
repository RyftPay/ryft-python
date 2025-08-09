import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.events import EventsClient
from ryft_sdk.models.errors import RyftError

from test.events.mock_data.mock_event_resp import mock_event_resp
from test.mock_error import mock_ryft_error

mock_event_id = "ev_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def events_client(mock_ryft_client):
    return EventsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_events_get(events_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_event_resp()
    resp = await events_client.get(mock_event_id, account="acc_123")
    mock_ryft_client.get.assert_called_once_with(
        f"events/{mock_event_id}", account="acc_123"
    )
    assert resp == mock_event_resp()


@pytest.mark.asyncio
async def test_events_get_error(events_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await events_client.get(mock_event_id)
