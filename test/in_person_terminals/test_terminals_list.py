from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_terminals import InPersonTerminalsClient
from test.in_person_terminals.mock_data.mock_terminal_resp import mock_terminals


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def terminals_client(mock_ryft_client):
    return InPersonTerminalsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_terminals_list(terminals_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_terminals()
    resp = await terminals_client.list()
    mock_ryft_client.get.assert_called_once_with(
        "in-person/terminals",
        {"ascending": None, "limit": None, "startsAfter": None},
        account=None,
    )
    assert resp == mock_terminals()
