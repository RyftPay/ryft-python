from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_sessions import PaymentSessionsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.payment_sessions.req.payment_sessions_req import (
    ContinuePaymentSessionRequest,
)
from typing import cast

from test.mock_error import mock_ryft_error
from test.payment_sessions.mock_data.mock_payment_sessions_continue_payment_req import (
    mock_continue_payment_req_submit_3ds_challenge_result,
    mock_continue_payment_req_submit_3ds_fingerprint_result,
)
from test.payment_sessions.mock_data.mock_payment_sessions_txs_resp import (
    mock_payment_sessions_txs_resp,
)

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payment_sessions_client(mock_ryft_client):
    return PaymentSessionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payment_sessions_continue_3ds_fingerprint(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        ContinuePaymentSessionRequest,
        mock_continue_payment_req_submit_3ds_fingerprint_result(),
    )
    resp = await payment_sessions_client.continue_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/continue-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_continue_3ds_challenge(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        ContinuePaymentSessionRequest,
        mock_continue_payment_req_submit_3ds_challenge_result(),
    )
    resp = await payment_sessions_client.continue_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/continue-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_continue_error(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(
        ContinuePaymentSessionRequest,
        mock_continue_payment_req_submit_3ds_fingerprint_result(),
    )
    with pytest.raises(RyftError):
        await payment_sessions_client.continue_payment(req)
