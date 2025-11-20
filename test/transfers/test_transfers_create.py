from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.transfers import TransfersClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.transfers.req.transfers_req import CreateTransferRequest
from typing import cast

from test.mock_error import mock_ryft_error
from test.transfers.mock_data.mock_transfers_create_req import (
    mock_create_transfer_req_pull_money_from_sub_account,
    mock_create_transfer_req_send_to_sub_account,
)
from test.transfers.mock_data.mock_transfers_resp import mock_transfer_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def transfers_client(mock_ryft_client):
    return TransfersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_transfers_transfer_from_sub_account(transfers_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_transfer_resp()
    req = cast(
        CreateTransferRequest, mock_create_transfer_req_pull_money_from_sub_account()
    )
    resp = await transfers_client.create(req)
    mock_ryft_client.post.assert_called_once_with("transfers", req)
    assert resp == mock_transfer_resp()


@pytest.mark.asyncio
async def test_transfers_transfer_to_sub_account(transfers_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_transfer_resp()
    req = cast(CreateTransferRequest, mock_create_transfer_req_send_to_sub_account())
    resp = await transfers_client.create(req)
    mock_ryft_client.post.assert_called_once_with("transfers", req)
    assert resp == mock_transfer_resp()


@pytest.mark.asyncio
async def test_transfers_transfer_error(transfers_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(
        CreateTransferRequest, mock_create_transfer_req_pull_money_from_sub_account()
    )
    with pytest.raises(RyftError):
        await transfers_client.create(req)
