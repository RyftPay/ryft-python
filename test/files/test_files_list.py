import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.files import FilesClient
from ryft_sdk.models.errors import RyftError
from test.files.mock_data.mock_files_resp import mock_files_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def files_client(mock_ryft_client):
    return FilesClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_files_list_default_params(files_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_files_resp()
    resp = await files_client.list()
    mock_ryft_client.get.assert_called_once_with(
        f"files",
        {
            "category": None,
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
    )
    assert resp == mock_files_resp()


@pytest.mark.asyncio
async def test_files_list_custom_params(files_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_files_resp()
    resp = await files_client.list(
        category="test", ascending=True, limit=10, startsAfter="foo"
    )
    mock_ryft_client.get.assert_called_once_with(
        f"files",
        {
            "category": "test",
            "ascending": True,
            "limit": 10,
            "startsAfter": "foo",
        },
    )
    assert resp == mock_files_resp()


@pytest.mark.asyncio
async def test_files_list_error(files_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await files_client.list()
