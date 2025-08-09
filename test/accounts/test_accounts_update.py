import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.accounts import AccountsClient
from ryft_sdk.models.accounts.req.accounts_req import UpdateSubAccountRequest
from ryft_sdk.models.errors import RyftError
from test.accounts.mock_data import mock_update_account_req
from typing import cast
from test.accounts.mock_data.mock_update_account_req import mock_update_account_req

from test.accounts.mock_data.mock_sub_account_resp import mock_sub_account_resp
from test.mock_error import mock_ryft_error

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def accounts_client(mock_ryft_client):
    return AccountsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_accounts_update(accounts_client, mock_ryft_client):
    mock_ryft_client.patch.return_value = mock_sub_account_resp()
    req = cast(UpdateSubAccountRequest, mock_update_account_req())
    resp = await accounts_client.update(mock_account_id, req)
    mock_ryft_client.patch.assert_called_once_with(f"accounts/{mock_account_id}", req)
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_update_error(accounts_client, mock_ryft_client):
    mock_ryft_client.patch.side_effect = mock_ryft_error()
    req = cast(UpdateSubAccountRequest, mock_update_account_req())
    with pytest.raises(RyftError):
        await accounts_client.update(mock_account_id, req)
