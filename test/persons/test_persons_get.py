from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.persons import PersonsClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.persons.mock_data.mock_persons_resp import mock_person_resp

mock_account_id = "acc_123"
mock_person_id = "per_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def persons_client(mock_ryft_client):
    return PersonsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_persons_get(persons_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_person_resp()
    resp = await persons_client.get(mock_account_id, mock_person_id)
    mock_ryft_client.get.assert_called_once_with(
        f"accounts/{mock_account_id}/persons/{mock_person_id}"
    )
    assert resp == mock_person_resp()


@pytest.mark.asyncio
async def test_persons_get_error(persons_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await persons_client.get(mock_account_id, mock_person_id)
