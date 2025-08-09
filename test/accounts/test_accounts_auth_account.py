import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.accounts import AccountsClient
from ryft_sdk.models.accounts.dto.accounts import AccountAuthorization
from ryft_sdk.models.errors import RyftError
from typing import cast
from ryft_sdk.models.errors import RyftError
from test.accounts.mock_data.mock_account_auth_resp import mock_account_auth_resp
from test.accounts.mock_data.mock_create_link_req import mock_create_link_req
from test.mock_error import mock_ryft_error

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def accounts_client(mock_ryft_client):
    return AccountsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_accounts_create_auth_link(accounts_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_account_auth_resp()
    req = cast(AccountAuthorization, mock_create_link_req())
    resp = await accounts_client.create_auth_link(req)
    mock_ryft_client.post.assert_called_once_with(f"accounts/authorize", req)
    assert resp == mock_account_auth_resp()


@pytest.mark.asyncio
async def test_accounts_create_auth_link_error(accounts_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(AccountAuthorization, mock_create_link_req())
    with pytest.raises(RyftError):
        await accounts_client.create_auth_link(req)
