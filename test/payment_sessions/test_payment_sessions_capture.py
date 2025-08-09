import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_sessions import PaymentSessionsClient
from ryft_sdk.models.errors import RyftError
from typing import cast

from ryft_sdk.models.payment_sessions.req.payment_sessions_transactions_req import (
    CapturePaymentSessionRequest,
)
from test.mock_error import mock_ryft_error
from test.payment_sessions.mock_data.mock_payment_sessions_capture_payment_req import (
    mock_capture_payment_req_with_partial_amount,
    mock_capture_payment_req_with_multi_capture_non_final,
    mock_capture_payment_req_with_split_payments,
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
async def test_payment_sessions_capture_with_non_final(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        CapturePaymentSessionRequest,
        mock_capture_payment_req_with_multi_capture_non_final(),
    )
    resp = await payment_sessions_client.capture(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/captures",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_capture_with_split_payments(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        CapturePaymentSessionRequest, mock_capture_payment_req_with_split_payments()
    )
    resp = await payment_sessions_client.capture(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/captures",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_capture_with_partial_amount(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        CapturePaymentSessionRequest, mock_capture_payment_req_with_partial_amount()
    )
    resp = await payment_sessions_client.capture(
        mock_payment_session_id, req, account=mock_account_id
    )
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/captures",
        req,
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_capture_error(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(
        CapturePaymentSessionRequest, mock_capture_payment_req_with_split_payments()
    )
    with pytest.raises(RyftError):
        await payment_sessions_client.capture(mock_payment_session_id, req)
