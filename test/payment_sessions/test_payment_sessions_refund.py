import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_sessions import PaymentSessionsClient
from ryft_sdk.models.errors import RyftError
from typing import cast

from ryft_sdk.models.payment_sessions.req.payment_sessions_transactions_req import (
    RefundPaymentSessionRequest,
)
from test.mock_error import mock_ryft_error
from test.payment_sessions.mock_data.mock_payment_sessions_refund_req import (
    mock_refund_req_marketplace_full_refund_split_payment,
    mock_refund_req_marketplace_partial_refund_split_payment,
    mock_refund_req_partial_refund,
    mock_refund_req_multi_capture_tx,
    mock_refund_req_with_reason,
    mock_refund_req_marketplace_refund_platform_fee,
)
from test.payment_sessions.mock_data.mock_payment_sessions_txs_resp import (
    mock_payment_sessions_txs_resp,
)

mock_account_id = "acc_123"
mock_payment_session_id = "pay_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payment_sessions_client(mock_ryft_client):
    return PaymentSessionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payment_sessions_refund_partial(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(RefundPaymentSessionRequest, mock_refund_req_partial_refund())
    resp = await payment_sessions_client.refund(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/refunds",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_refund_with_reason(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(RefundPaymentSessionRequest, mock_refund_req_with_reason())
    resp = await payment_sessions_client.refund(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/refunds",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_refund_multi_capture_tx(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(RefundPaymentSessionRequest, mock_refund_req_multi_capture_tx())
    resp = await payment_sessions_client.refund(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/refunds",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_refund_platform_fee(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        RefundPaymentSessionRequest, mock_refund_req_marketplace_refund_platform_fee()
    )
    resp = await payment_sessions_client.refund(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/refunds",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_refund_partial_split_payments(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        RefundPaymentSessionRequest,
        mock_refund_req_marketplace_partial_refund_split_payment(),
    )
    resp = await payment_sessions_client.refund(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/refunds",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_refund_full_split_payments(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        RefundPaymentSessionRequest,
        mock_refund_req_marketplace_full_refund_split_payment(),
    )
    resp = await payment_sessions_client.refund(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/refunds",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_refund_error(payment_sessions_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(RefundPaymentSessionRequest, mock_refund_req_with_reason())
    with pytest.raises(RyftError):
        await payment_sessions_client.refund(mock_payment_session_id, req)
