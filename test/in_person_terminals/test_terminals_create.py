from __future__ import annotations

import pytest
from typing import cast
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_terminals import InPersonTerminalsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.in_person_terminals.req.in_person_terminals_req import (
    CreateTerminalRequest,
)
from test.in_person_terminals.mock_data.mock_terminal_resp import (
    mock_terminal,
    mock_create_terminal_req,
)
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def terminals_client(mock_ryft_client):
    return InPersonTerminalsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_terminals_create(terminals_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_terminal()
    req = cast(CreateTerminalRequest, mock_create_terminal_req())
    resp = await terminals_client.create(req)
    mock_ryft_client.post.assert_called_once_with(
        "in-person/terminals", req, account=None
    )
    assert resp == mock_terminal()


@pytest.mark.asyncio
async def test_terminals_create_with_account(terminals_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_terminal()
    req = cast(CreateTerminalRequest, mock_create_terminal_req())
    resp = await terminals_client.create(
        req, account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327"
    )
    mock_ryft_client.post.assert_called_once_with(
        "in-person/terminals", req, account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327"
    )
    assert resp == mock_terminal()


@pytest.mark.asyncio
async def test_terminals_create_error(terminals_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreateTerminalRequest, mock_create_terminal_req())
    with pytest.raises(RyftError):
        await terminals_client.create(req)
