import pytest
from typing import cast
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_locations import InPersonLocationsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.in_person_locations.req.in_person_locations_req import (
    CreateInPersonLocationRequest,
)
from test.in_person_locations.mock_data.mock_location_resp import (
    mock_in_person_location,
    mock_create_location_req,
)
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def locations_client(mock_ryft_client):
    return InPersonLocationsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_locations_create(locations_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_in_person_location()
    req = cast(CreateInPersonLocationRequest, mock_create_location_req())
    resp = await locations_client.create(req)
    mock_ryft_client.post.assert_called_once_with(
        "in-person/locations", req, account=None
    )
    assert resp == mock_in_person_location()


@pytest.mark.asyncio
async def test_locations_create_with_account(locations_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_in_person_location()
    req = cast(CreateInPersonLocationRequest, mock_create_location_req())
    resp = await locations_client.create(
        req, account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327"
    )
    mock_ryft_client.post.assert_called_once_with(
        "in-person/locations", req, account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327"
    )
    assert resp == mock_in_person_location()


@pytest.mark.asyncio
async def test_locations_create_error(locations_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreateInPersonLocationRequest, mock_create_location_req())
    with pytest.raises(RyftError):
        await locations_client.create(req)
