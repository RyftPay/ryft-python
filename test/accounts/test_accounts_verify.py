import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.accounts import AccountsClient
from ryft_sdk.models.errors import RyftError

from test.accounts.mock_data.mock_sub_account_resp import mock_sub_account_resp
from test.mock_error import mock_ryft_error

mock__account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def accounts_client(mock_ryft_client):
    return AccountsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_accounts_verify(accounts_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_sub_account_resp()
    resp = await accounts_client.verify(mock__account_id)
    mock_ryft_client.post.assert_called_once_with(
        f"accounts/{mock__account_id}/verify", {}
    )
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_verify_error(accounts_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await accounts_client.verify(mock__account_id)
