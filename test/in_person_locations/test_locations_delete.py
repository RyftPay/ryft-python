import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_locations import InPersonLocationsClient
from ryft_sdk.models.errors import RyftError
from test.mock_deleted_resource_resp import mock_deleted_resource_resp
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def locations_client(mock_ryft_client):
    return InPersonLocationsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_locations_delete(locations_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await locations_client.delete("iploc_01FCTS1XMKH9FF43CAFA4CXT3P")
    mock_ryft_client.delete.assert_called_once_with(
        "in-person/locations/iploc_01FCTS1XMKH9FF43CAFA4CXT3P", {}, account=None
    )
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_locations_delete_with_account(locations_client, mock_ryft_client):
    mock_ryft_client.delete.return_value = mock_deleted_resource_resp()
    resp = await locations_client.delete(
        "iploc_01FCTS1XMKH9FF43CAFA4CXT3P",
        account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327",
    )
    mock_ryft_client.delete.assert_called_once_with(
        "in-person/locations/iploc_01FCTS1XMKH9FF43CAFA4CXT3P",
        {},
        account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327",
    )
    assert resp == mock_deleted_resource_resp()


@pytest.mark.asyncio
async def test_locations_delete_error(locations_client, mock_ryft_client):
    mock_ryft_client.delete.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await locations_client.delete("iploc_01FCTS1XMKH9FF43CAFA4CXT3P")
