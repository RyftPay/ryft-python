import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_sessions import PaymentSessionsClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.payment_sessions.mock_data.mock_payment_sessions_txs_resp import (
    mock_payment_sessions_txs_resp,
)

mock_account_id = "acc_123"
mock_payment_session_id = "pay_123"
mock_transaction_id = "tx_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payment_sessions_client(mock_ryft_client):
    return PaymentSessionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payment_sessions_get_transaction(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.get.return_value = mock_payment_sessions_txs_resp()
    resp = await payment_sessions_client.get_transaction(
        mock_payment_session_id, mock_transaction_id, account=mock_account_id
    )
    mock_ryft_client.get.assert_called_once_with(
        f"payment-sessions/{mock_payment_session_id}/transactions/{mock_transaction_id}",
        account=mock_account_id,
    )
    assert resp == mock_payment_sessions_txs_resp()


@pytest.mark.asyncio
async def test_payment_sessions_get_transaction_error(
    payment_sessions_client, mock_ryft_client
):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await payment_sessions_client.get_transaction(
            mock_payment_session_id, mock_transaction_id, account=mock_account_id
        )
