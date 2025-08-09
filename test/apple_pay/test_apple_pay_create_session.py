import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.apple_pay import ApplePayClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.apple_pay.req.apple_pay_req import CreateApplePayWebSessionReq
from test.apple_pay.mock_data.mock_apple_pay_create_session_req import (
    mock_apple_pay_create_session_req,
)
from test.apple_pay.mock_data.mock_apple_pay_session_resp import (
    mock_apple_pay_session_resp,
)
from test.mock_error import mock_ryft_error
from typing import cast

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def apple_pay_client(mock_ryft_client):
    return ApplePayClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_apple_pay_create_session(apple_pay_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_apple_pay_session_resp()
    req = cast(CreateApplePayWebSessionReq, mock_apple_pay_create_session_req())
    resp = await apple_pay_client.create_session(req)
    mock_ryft_client.post.assert_called_once_with("apple-pay/sessions", cast(dict, req))
    assert resp == mock_apple_pay_session_resp()


@pytest.mark.asyncio
async def test_apple_pay_create_session_error(apple_pay_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        req = cast(CreateApplePayWebSessionReq, mock_apple_pay_create_session_req())
        await apple_pay_client.create_session(req)
