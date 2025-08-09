import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.persons import PersonsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.persons.req.persons_req import CreatePersonRequest
from typing import cast
from test.mock_error import mock_ryft_error
from test.persons.mock_data.mock_persons_create_req import mock_create_persons_req
from test.persons.mock_data.mock_persons_resp import mock_person_resp

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def persons_client(mock_ryft_client):
    return PersonsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_persons_create(persons_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_person_resp()
    req = cast(CreatePersonRequest, mock_create_persons_req())
    resp = await persons_client.create(mock_account_id, req)
    mock_ryft_client.post.assert_called_once_with(
        f"accounts/{mock_account_id}/persons", req
    )
    assert resp == mock_person_resp()


@pytest.mark.asyncio
async def test_persons_create_error(persons_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreatePersonRequest, mock_create_persons_req())
    with pytest.raises(RyftError):
        await persons_client.create(mock_account_id, req)
