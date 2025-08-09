import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.files import FilesClient
from ryft_sdk.models.errors import RyftError
from test.files.mock_data.mock_files_create_req import mock_create_file_req
from test.files.mock_data.mock_files_resp import mock_file_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def files_client(mock_ryft_client):
    return FilesClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_files_create(files_client, mock_ryft_client):
    mock_ryft_client.upload_file.return_value = mock_file_resp()
    resp = await files_client.create(mock_create_file_req(), account="acc_123")
    mock_ryft_client.upload_file.assert_called_once_with(
        endpoint="files",
        file_path=mock_create_file_req().get("file"),
        category=mock_create_file_req().get("category"),
        account="acc_123",
    )
    assert resp == mock_file_resp()


@pytest.mark.asyncio
async def test_files_create_error(files_client, mock_ryft_client):
    mock_ryft_client.upload_file.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await files_client.create(mock_create_file_req())
