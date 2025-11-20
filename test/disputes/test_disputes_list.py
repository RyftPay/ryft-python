from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.disputes import DisputesClient
from ryft_sdk.models.errors import RyftError
from test.disputes.mock_data.mock_dispute_resp import mock_disputes_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def disputes_client(mock_ryft_client):
    return DisputesClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_disputes_list_with_defaults(disputes_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_disputes_resp()
    resp = await disputes_client.list()
    mock_ryft_client.get.assert_called_once_with(
        f"disputes",
        {
            "startTimestamp": None,
            "endTimestamp": None,
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
    )
    assert resp == mock_disputes_resp()


@pytest.mark.asyncio
async def test_disputes_list_with_params(disputes_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_disputes_resp()
    resp = await disputes_client.list(
        startTimestamp=1000,
        endTimestamp=2000,
        ascending=True,
        limit=20,
        startsAfter="foo",
    )
    mock_ryft_client.get.assert_called_once_with(
        f"disputes",
        {
            "startTimestamp": 1000,
            "endTimestamp": 2000,
            "ascending": True,
            "limit": 20,
            "startsAfter": "foo",
        },
    )
    assert resp == mock_disputes_resp()


@pytest.mark.asyncio
async def test_disputes_list_error(disputes_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await disputes_client.list()
