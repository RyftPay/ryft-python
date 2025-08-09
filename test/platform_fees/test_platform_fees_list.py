import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.platform_fees import PlatformFeesClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.platform_fees.mock_data.mock_platform_fees_resp import mock_platform_fees_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def platform_fees_client(mock_ryft_client):
    return PlatformFeesClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_platform_fees_list_with_default_params(
    platform_fees_client, mock_ryft_client
):
    mock_ryft_client.get.return_value = mock_platform_fees_resp()
    resp = await platform_fees_client.list()
    mock_ryft_client.get.assert_called_once_with(
        "platform-fees", {"ascending": None, "limit": None}
    )
    assert resp == mock_platform_fees_resp()


@pytest.mark.asyncio
async def test_platform_fees_list_with_custom_params(
    platform_fees_client, mock_ryft_client
):
    mock_ryft_client.get.return_value = mock_platform_fees_resp()
    resp = await platform_fees_client.list(ascending=True, limit=10)
    mock_ryft_client.get.assert_called_once_with(
        "platform-fees", {"ascending": True, "limit": 10}
    )
    assert resp == mock_platform_fees_resp()


@pytest.mark.asyncio
async def test_platform_fees_list_error(platform_fees_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await platform_fees_client.list()
