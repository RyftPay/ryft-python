from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_skus import InPersonSkusClient
from ryft_sdk.models.errors import RyftError
from test.in_person_skus.mock_data.mock_sku_resp import mock_in_person_sku
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def skus_client(mock_ryft_client):
    return InPersonSkusClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_skus_get(skus_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_sku()
    resp = await skus_client.get("ipsku_01FCTS1XMKH9FF43CAFA4CXT3P")
    mock_ryft_client.get.assert_called_once_with(
        "in-person/skus/ipsku_01FCTS1XMKH9FF43CAFA4CXT3P"
    )
    assert resp == mock_in_person_sku()


@pytest.mark.asyncio
async def test_skus_get_error(skus_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await skus_client.get("ipsku_01FCTS1XMKH9FF43CAFA4CXT3P")
