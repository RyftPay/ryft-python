from __future__ import annotations

import pytest
from typing import cast
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_terminals import InPersonTerminalsClient
from ryft_sdk.models.in_person_terminals.req.in_person_terminals_req import (
    TerminalPaymentRequest,
    TerminalRefundRequest,
    TerminalConfirmReceiptRequest,
)
from test.in_person_terminals.mock_data.mock_terminal_resp import (
    mock_terminal,
    mock_payment_req,
    mock_refund_req,
    mock_confirm_receipt_req,
)


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def terminals_client(mock_ryft_client):
    return InPersonTerminalsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_terminals_init_payment(terminals_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_terminal()
    req = cast(TerminalPaymentRequest, mock_payment_req())
    resp = await terminals_client.init_payment("tml_01FCTS1XMKH9FF43CAFA4CXT3P", req)
    mock_ryft_client.post.assert_called_once_with(
        "in-person/terminals/tml_01FCTS1XMKH9FF43CAFA4CXT3P/payment", req, account=None
    )
    assert resp == mock_terminal()


@pytest.mark.asyncio
async def test_terminals_init_refund(terminals_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_terminal()
    req = cast(TerminalRefundRequest, mock_refund_req())
    resp = await terminals_client.init_refund("tml_01FCTS1XMKH9FF43CAFA4CXT3P", req)
    mock_ryft_client.post.assert_called_once_with(
        "in-person/terminals/tml_01FCTS1XMKH9FF43CAFA4CXT3P/refund", req, account=None
    )
    assert resp == mock_terminal()


@pytest.mark.asyncio
async def test_terminals_cancel_action(terminals_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_terminal()
    resp = await terminals_client.cancel_action("tml_01FCTS1XMKH9FF43CAFA4CXT3P")
    mock_ryft_client.post.assert_called_once_with(
        "in-person/terminals/tml_01FCTS1XMKH9FF43CAFA4CXT3P/cancel-action",
        {},
        account=None,
    )
    assert resp == mock_terminal()


@pytest.mark.asyncio
async def test_terminals_confirm_receipt(terminals_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_terminal()
    req = cast(TerminalConfirmReceiptRequest, mock_confirm_receipt_req())
    resp = await terminals_client.confirm_receipt("tml_01FCTS1XMKH9FF43CAFA4CXT3P", req)
    mock_ryft_client.post.assert_called_once_with(
        "in-person/terminals/tml_01FCTS1XMKH9FF43CAFA4CXT3P/confirm-receipt",
        req,
        account=None,
    )
    assert resp == mock_terminal()
