from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payout_methods import PayoutMethodsClient
from ryft_sdk.models.errors import RyftError
from test.mock_deleted_resource_resp import mock_deleted_resource_resp
from test.mock_error import mock_ryft_error


mock_account_id = "acc_123"
mock_payout_method_id = "pmt_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payout_methods_client(mock_ryft_client):
    return PayoutMethodsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payout_methods_delete(payout_methods_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await payout_methods_client.delete(mock_account_id, mock_payout_method_id)
    mock_ryft_client.delete.assert_called_once_with(
        f"accounts/{mock_account_id}/payout-methods/{mock_payout_method_id}", {}
    )
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_payout_methods_delete_error(payout_methods_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await payout_methods_client.delete(mock_account_id, mock_payout_method_id)
