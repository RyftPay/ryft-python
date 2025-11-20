from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_terminals import InPersonTerminalsClient
from test.in_person_terminals.mock_data.mock_terminal_resp import mock_terminal


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def terminals_client(mock_ryft_client):
    return InPersonTerminalsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_terminals_get(terminals_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_terminal()
    resp = await terminals_client.get("tml_01FCTS1XMKH9FF43CAFA4CXT3P")
    mock_ryft_client.get.assert_called_once_with(
        "in-person/terminals/tml_01FCTS1XMKH9FF43CAFA4CXT3P", account=None
    )
    assert resp == mock_terminal()
