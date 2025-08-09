import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.account_links import AccountLinksClient
from ryft_sdk.models.account_links.req.account_links_req import CreateTmpLinkReq
from ryft_sdk.models.errors import RyftError
from test.account_links.mock_data.mock_account_links_resp import mock_account_links_resp
from test.account_links.mock_data.mock_create_tmp_link_req import (
    mock_create_tmp_link_req,
)
from typing import cast
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def account_links_client(mock_ryft_client):
    return AccountLinksClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_account_links_create_tmp_link(account_links_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_account_links_resp()
    req = cast(CreateTmpLinkReq, mock_create_tmp_link_req())
    resp = await account_links_client.create_tmp_link(req)
    mock_ryft_client.post.assert_called_once_with("account-links", req)
    assert resp == mock_account_links_resp()


@pytest.mark.asyncio
async def test_account_links_create_tmp_link_error(
    account_links_client, mock_ryft_client
):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreateTmpLinkReq, mock_create_tmp_link_req())
    with pytest.raises(RyftError):
        await account_links_client.create_tmp_link(req)
