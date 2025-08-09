import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.disputes import DisputesClient
from ryft_sdk.models.errors import RyftError
from test.disputes.mock_data.mock_dispute_resp import mock_dispute_resp
from test.mock_error import mock_ryft_error

mock_dispute_id = "do_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def disputes_client(mock_ryft_client):
    return DisputesClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_disputes_accept(disputes_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_dispute_resp()
    resp = await disputes_client.accept(mock_dispute_id)
    mock_ryft_client.post.assert_called_once_with(
        f"disputes/{mock_dispute_id}/accept", {}
    )
    assert resp == mock_dispute_resp()


@pytest.mark.asyncio
async def test_disputes_accept_error(disputes_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await disputes_client.accept(mock_dispute_id)
