from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payout_methods import PayoutMethodsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.payout_methods.req.payout_methods import (
    UpdatePayoutMethodRequest,
)
from typing import cast
from test.mock_error import mock_ryft_error
from test.payout_methods.mock_data.mock_payout_methods_resp import (
    mock_payout_method_resp,
)
from test.payout_methods.mock_data.mock_payout_methods_update_req import (
    mock_update_payout_method_req,
)


mock_account_id = "acc_123"
mock_payout_method_id = "pmt_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payout_methods_client(mock_ryft_client):
    return PayoutMethodsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payout_methods_update(payout_methods_client, mock_ryft_client):
    mock_ryft_client.patch.return_value = mock_payout_method_resp()
    req = cast(UpdatePayoutMethodRequest, mock_update_payout_method_req())
    resp = await payout_methods_client.update(
        mock_account_id, mock_payout_method_id, req
    )
    mock_ryft_client.patch.assert_called_once_with(
        f"accounts/{mock_account_id}/payout-methods/{mock_payout_method_id}", req
    )
    assert resp == mock_payout_method_resp()


@pytest.mark.asyncio
async def test_payout_methods_update_error(payout_methods_client, mock_ryft_client):
    mock_ryft_client.patch.side_effect = mock_ryft_error()
    req = cast(UpdatePayoutMethodRequest, mock_update_payout_method_req())
    with pytest.raises(RyftError):
        await payout_methods_client.update(mock_account_id, mock_payout_method_id, req)
