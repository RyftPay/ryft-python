from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payout_methods import PayoutMethodsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.payout_methods.req.payout_methods import (
    CreatePayoutMethodRequest,
)
from typing import cast
from test.mock_error import mock_ryft_error
from test.payout_methods.mock_data.mock_payout_methods_create_req import (
    mock_create_payout_method_req_eur_bank_acc,
    mock_create_payout_method_req_gbp_bank_acc,
    mock_create_payout_method_req_us_bank_acc,
)
from test.payout_methods.mock_data.mock_payout_methods_resp import (
    mock_payout_method_resp,
)


mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payout_methods_client(mock_ryft_client):
    return PayoutMethodsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payout_methods_create_gbp_account(
    payout_methods_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payout_method_resp()
    req = cast(CreatePayoutMethodRequest, mock_create_payout_method_req_gbp_bank_acc())
    resp = await payout_methods_client.create(mock_account_id, req)
    mock_ryft_client.post.assert_called_once_with(
        f"accounts/{mock_account_id}/payout-methods", req
    )
    assert resp == mock_payout_method_resp()


@pytest.mark.asyncio
async def test_payout_methods_create_eur_account(
    payout_methods_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payout_method_resp()
    req = cast(CreatePayoutMethodRequest, mock_create_payout_method_req_eur_bank_acc())
    resp = await payout_methods_client.create(mock_account_id, req)
    mock_ryft_client.post.assert_called_once_with(
        f"accounts/{mock_account_id}/payout-methods", req
    )
    assert resp == mock_payout_method_resp()


@pytest.mark.asyncio
async def test_payout_methods_create_usd_account(
    payout_methods_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_payout_method_resp()
    req = cast(CreatePayoutMethodRequest, mock_create_payout_method_req_us_bank_acc())
    resp = await payout_methods_client.create(mock_account_id, req)
    mock_ryft_client.post.assert_called_once_with(
        f"accounts/{mock_account_id}/payout-methods", req
    )
    assert resp == mock_payout_method_resp()


@pytest.mark.asyncio
async def test_payout_methods_create_error(payout_methods_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreatePayoutMethodRequest, mock_create_payout_method_req_eur_bank_acc())
    with pytest.raises(RyftError):
        await payout_methods_client.create(mock_account_id, req)
