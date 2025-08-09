import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_sessions import PaymentSessionsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.payment_sessions.req.payment_sessions_req import (
    AttemptPaymentSessionRequest,
)
from typing import cast

from test.mock_error import mock_ryft_error
from test.payment_sessions.mock_data.mock_payment_sessions_attempt_payment_req import (
    mock_attempt_payment_req_with_3ds,
    mock_attempt_payment_req_with_apple_pay_token,
    mock_attempt_payment_req_with_billing_address_included,
    mock_attempt_payment_req_with_card,
    mock_attempt_payment_req_with_card_and_save,
    mock_attempt_payment_req_with_customer_included,
    mock_attempt_payment_req_with_google_pay_token,
    mock_attempt_payment_req_with_saved_payment_method,
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
async def test_payment_sessions_attempt_with_card(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(AttemptPaymentSessionRequest, mock_attempt_payment_req_with_card())
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_with_card_and_save(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        AttemptPaymentSessionRequest, mock_attempt_payment_req_with_card_and_save()
    )
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_with_card_and_saved_payment_method(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        AttemptPaymentSessionRequest,
        mock_attempt_payment_req_with_saved_payment_method(),
    )
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_google_pay_token(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        AttemptPaymentSessionRequest, mock_attempt_payment_req_with_google_pay_token()
    )
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_apple_pay_token(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        AttemptPaymentSessionRequest, mock_attempt_payment_req_with_apple_pay_token()
    )
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_with_billing_address(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        AttemptPaymentSessionRequest,
        mock_attempt_payment_req_with_billing_address_included(),
    )
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_with_customer_included(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(
        AttemptPaymentSessionRequest, mock_attempt_payment_req_with_customer_included()
    )
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_with_3ds(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payment_sessions_txs_resp()
    req = cast(AttemptPaymentSessionRequest, mock_attempt_payment_req_with_3ds())
    resp = await payment_sessions_client.attempt_payment(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"payment-sessions/attempt-payment", req, account=mock_account_id
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_attempt_error(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(AttemptPaymentSessionRequest, mock_attempt_payment_req_with_3ds())
    with pytest.raises(RyftError):
        await payment_sessions_client.attempt_payment(req)
