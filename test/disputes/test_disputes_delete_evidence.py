from typing import cast
import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.disputes import DisputesClient
from ryft_sdk.models.disputes.req.disputes_req import DeleteDisputeEvidenceRequest
from ryft_sdk.models.errors import RyftError
from test.disputes.mock_data.mock_delete_dispute_evidence_req import (
    mock_delete_dispute_evidence_req,
)
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
async def test_disputes_deleet_evidence(disputes_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_dispute_resp()
    req = cast(DeleteDisputeEvidenceRequest, mock_delete_dispute_evidence_req())
    resp = await disputes_client.delete_evidence(mock_dispute_id, req)
    mock_ryft_client.delete.assert_called_once_with(
        f"disputes/{mock_dispute_id}/evidence", mock_delete_dispute_evidence_req()
    )
    assert resp == mock_dispute_resp()


@pytest.mark.asyncio
async def test_disputes_add_evidence_error(disputes_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        req = cast(DeleteDisputeEvidenceRequest, mock_delete_dispute_evidence_req())
        await disputes_client.delete_evidence(mock_dispute_id, req)
