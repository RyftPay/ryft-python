from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.files import FilesClient
from ryft_sdk.models.errors import RyftError
from test.files.mock_data.mock_files_resp import mock_file_resp
from test.mock_error import mock_ryft_error

mock_file_id = "fl_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def files_client(mock_ryft_client):
    return FilesClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_files_get(files_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_file_resp()
    resp = await files_client.get(mock_file_id)
    mock_ryft_client.get.assert_called_once_with(f"files/{mock_file_id}", account=None)
    assert resp == mock_file_resp()


@pytest.mark.asyncio
async def test_files_get_error(files_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await files_client.get(mock_file_id)
