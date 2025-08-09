import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.accounts import AccountsClient
from ryft_sdk.models.errors import RyftError
from test.accounts.mock_data.mock_payout_resp import mock_payout_resp
from test.mock_error import mock_ryft_error

mock_account_id = "acc_123"
mock_payout_id = "po_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def accounts_client(mock_ryft_client):
    return AccountsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_accounts_get_payout(accounts_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_payout_resp()
    resp = await accounts_client.get_payout(mock_account_id, mock_payout_id)
    mock_ryft_client.get.assert_called_once_with(
        f"accounts/{mock_account_id}/payouts/{mock_payout_id}"
    )
    assert resp == mock_payout_resp()


@pytest.mark.asyncio
async def test_accounts_get_payout_error(accounts_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await accounts_client.get_payout(mock_account_id, mock_payout_id)
