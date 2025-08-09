import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.accounts import AccountsClient
from ryft_sdk.models.errors import RyftError
from test.accounts.mock_data.mock_payout_resp import mock_payouts_resp
from test.mock_error import mock_ryft_error

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def accounts_client(mock_ryft_client):
    return AccountsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_accounts_list_payouts_with_defaults(accounts_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_payouts_resp()
    resp = await accounts_client.list_payouts(mock_account_id)
    mock_ryft_client.get.assert_called_once_with(
        f"accounts/{mock_account_id}/payouts",
        {
            "start": None,
            "end": None,
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
    )
    assert resp == mock_payouts_resp()


@pytest.mark.asyncio
async def test_accounts_list_payouts_with_params(accounts_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_payouts_resp()
    resp = await accounts_client.list_payouts(
        mock_account_id,
        start=1000,
        end=2000,
        ascending=True,
        limit=20,
        startsAfter="foo",
    )
    mock_ryft_client.get.assert_called_once_with(
        f"accounts/{mock_account_id}/payouts",
        {
            "start": 1000,
            "end": 2000,
            "ascending": True,
            "limit": 20,
            "startsAfter": "foo",
        },
    )
    assert resp == mock_payouts_resp()


@pytest.mark.asyncio
async def test_accounts_list_payouts_error(accounts_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await accounts_client.list_payouts(mock_account_id, {})
