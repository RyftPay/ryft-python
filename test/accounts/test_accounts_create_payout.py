from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.accounts import AccountsClient
from ryft_sdk.models.accounts.req.payouts_req import CreatePayoutRequest
from ryft_sdk.models.errors import RyftError
from test.accounts.mock_data import mock_create_payout_req
from typing import cast
from test.accounts.mock_data.mock_create_payout_req import mock_create_payout_req

from test.accounts.mock_data.mock_payout_resp import mock_payout_resp
from test.mock_error import mock_ryft_error

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def accounts_client(mock_ryft_client):
    return AccountsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_accounts_create_payout(accounts_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_payout_resp()
    req = cast(CreatePayoutRequest, mock_create_payout_req())
    resp = await accounts_client.create_payout(mock_account_id, req)
    mock_ryft_client.post.assert_called_once_with(
        f"accounts/{mock_account_id}/payouts", req
    )
    assert resp == mock_payout_resp()


@pytest.mark.asyncio
async def test_accounts_create_payout_error(accounts_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreatePayoutRequest, mock_create_payout_req())
    with pytest.raises(RyftError):
        await accounts_client.create_payout(mock_account_id, req)
