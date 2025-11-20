from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_locations import InPersonLocationsClient
from ryft_sdk.models.errors import RyftError
from test.in_person_locations.mock_data.mock_location_resp import (
    mock_in_person_location,
)
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def locations_client(mock_ryft_client):
    return InPersonLocationsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_locations_get(locations_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_location()
    resp = await locations_client.get("iploc_01FCTS1XMKH9FF43CAFA4CXT3P")
    mock_ryft_client.get.assert_called_once_with(
        "in-person/locations/iploc_01FCTS1XMKH9FF43CAFA4CXT3P", account=None
    )
    assert resp == mock_in_person_location()


@pytest.mark.asyncio
async def test_locations_get_with_account(locations_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_location()
    resp = await locations_client.get(
        "iploc_01FCTS1XMKH9FF43CAFA4CXT3P",
        account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327",
    )
    mock_ryft_client.get.assert_called_once_with(
        "in-person/locations/iploc_01FCTS1XMKH9FF43CAFA4CXT3P",
        account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327",
    )
    assert resp == mock_in_person_location()


@pytest.mark.asyncio
async def test_locations_get_error(locations_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await locations_client.get("iploc_01FCTS1XMKH9FF43CAFA4CXT3P")
