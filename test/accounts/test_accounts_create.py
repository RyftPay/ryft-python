import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.accounts import AccountsClient
from ryft_sdk.models.accounts.req.accounts_req import CreateSubAccountRequest
from ryft_sdk.models.errors import RyftError
from test.accounts.mock_data.mock_create_account_req import (
    mock_create_account_request_hosted_onboarding_business,
    mock_create_account_request_hosted_onboarding_individual,
    mock_create_account_request_hosted_onboarding_minimum,
    mock_create_account_request_non_hosted_onboarding_business,
    mock_create_account_request_non_hosted_onboarding_individual,
    mock_create_account_request_non_hosted_onboarding_minimum,
)
from typing import cast

from test.accounts.mock_data.mock_sub_account_resp import mock_sub_account_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def accounts_client(mock_ryft_client):
    return AccountsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_accounts_create_success_hosted_onboarding_minimum(
    accounts_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_sub_account_resp()
    req = cast(
        CreateSubAccountRequest, mock_create_account_request_hosted_onboarding_minimum()
    )
    resp = await accounts_client.create(req)
    mock_ryft_client.post.assert_called_once_with("accounts", req)
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_create_success_hosted_onboarding_business(
    accounts_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_sub_account_resp()
    req = cast(
        CreateSubAccountRequest,
        mock_create_account_request_hosted_onboarding_business(),
    )
    resp = await accounts_client.create(req)
    mock_ryft_client.post.assert_called_once_with("accounts", req)
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_create_success_hosted_onboarding_individual(
    accounts_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_sub_account_resp()
    req = cast(
        CreateSubAccountRequest,
        mock_create_account_request_hosted_onboarding_individual(),
    )
    resp = await accounts_client.create(req)
    mock_ryft_client.post.assert_called_once_with("accounts", req)
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_create_success_non_hosted_onboarding_minimum(
    accounts_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_sub_account_resp()
    req = cast(
        CreateSubAccountRequest,
        mock_create_account_request_non_hosted_onboarding_minimum(),
    )
    resp = await accounts_client.create(req)
    mock_ryft_client.post.assert_called_once_with("accounts", req)
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_create_success_non_hosted_onboarding_individual(
    accounts_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_sub_account_resp()
    req = cast(
        CreateSubAccountRequest,
        mock_create_account_request_non_hosted_onboarding_individual(),
    )
    resp = await accounts_client.create(req)
    mock_ryft_client.post.assert_called_once_with("accounts", req)
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_create_success_non_hosted_onboarding_business(
    accounts_client, mock_ryft_client
):
    mock_ryft_client.post.return_value = mock_sub_account_resp()
    req = cast(
        CreateSubAccountRequest,
        mock_create_account_request_non_hosted_onboarding_business(),
    )
    resp = await accounts_client.create(req)
    mock_ryft_client.post.assert_called_once_with("accounts", req)
    assert resp == mock_sub_account_resp()


@pytest.mark.asyncio
async def test_accounts_create_error(accounts_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(
        CreateSubAccountRequest, mock_create_account_request_hosted_onboarding_minimum()
    )
    with pytest.raises(RyftError):
        await accounts_client.create(req)
