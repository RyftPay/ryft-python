import pytest
from typing import cast
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_terminals import InPersonTerminalsClient
from ryft_sdk.models.in_person_terminals.req.in_person_terminals_req import (
    UpdateTerminalRequest,
)
from test.in_person_terminals.mock_data.mock_terminal_resp import (
    mock_terminal,
    mock_update_terminal_req,
)


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def terminals_client(mock_ryft_client):
    return InPersonTerminalsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_terminals_update(terminals_client, mock_ryft_client):
    mock_ryft_client.patch.return_value = mock_terminal()
    req = cast(UpdateTerminalRequest, mock_update_terminal_req())
    resp = await terminals_client.update("tml_01FCTS1XMKH9FF43CAFA4CXT3P", req)
    mock_ryft_client.patch.assert_called_once_with(
        "in-person/terminals/tml_01FCTS1XMKH9FF43CAFA4CXT3P", req, account=None
    )
    assert resp == mock_terminal()
