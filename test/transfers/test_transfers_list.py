from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.transfers import TransfersClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.transfers.mock_data.mock_transfers_resp import mock_transfers_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def transfers_client(mock_ryft_client):
    return TransfersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_transfers_list_with_defaults(transfers_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_transfers_resp()
    resp = await transfers_client.list()
    mock_ryft_client.get.assert_called_once_with(
        "transfers",
        {
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
    )
    assert resp == mock_transfers_resp()


@pytest.mark.asyncio
async def test_transfers_list_with_custom_params(transfers_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_transfers_resp()
    resp = await transfers_client.list(ascending=True, limit=10, startsAfter="12345")
    mock_ryft_client.get.assert_called_once_with(
        "transfers",
        {
            "ascending": True,
            "limit": 10,
            "startsAfter": "12345",
        },
    )
    assert resp == mock_transfers_resp()


@pytest.mark.asyncio
async def test_transfers_list_error(transfers_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await transfers_client.list()
