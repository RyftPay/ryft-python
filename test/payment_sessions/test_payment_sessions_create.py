from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_sessions import PaymentSessionsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.payment_sessions.req.payment_sessions_req import (
    CreatePaymentSessionRequest,
)
from typing import cast

from test.mock_error import mock_ryft_error
from test.payment_sessions.mock_data.mock_payment_sessions_create_req import (
    mock_create_payment_session_req,
)
from test.payment_sessions.mock_data.mock_payment_sessions_resp import (
    mock_payment_session_resp,
)

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payment_sessions_client(mock_ryft_client):
    return PaymentSessionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payment_sessions_create(payment_sessions_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_payment_session_resp()
    req = cast(CreatePaymentSessionRequest, mock_create_payment_session_req())
    resp = await payment_sessions_client.create(req, account=mock_account_id)
    mock_ryft_client.post.assert_called_once_with(
        "payment-sessions", req, account=mock_account_id
    )
    assert resp == mock_payment_session_resp()


@pytest.mark.asyncio
async def test_payment_sessions_create_error(payment_sessions_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreatePaymentSessionRequest, mock_create_payment_session_req())
    with pytest.raises(RyftError):
        await payment_sessions_client.create(req)
