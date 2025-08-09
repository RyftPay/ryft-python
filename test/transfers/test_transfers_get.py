import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.transfers import TransfersClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.transfers.mock_data.mock_transfers_resp import mock_transfer_resp

mock_transfer_id = "ts_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def transfers_client(mock_ryft_client):
    return TransfersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_transfers_get(transfers_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_transfer_resp()
    resp = await transfers_client.get(mock_transfer_id)
    mock_ryft_client.get.assert_called_once_with(f"transfers/{mock_transfer_id}")
    assert resp == mock_transfer_resp()


@pytest.mark.asyncio
async def test_transfers_get_error(transfers_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await transfers_client.get(mock_transfer_id)
