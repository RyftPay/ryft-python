from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_products import InPersonProductsClient
from ryft_sdk.models.errors import RyftError
from test.in_person_products.mock_data.mock_product_resp import (
    mock_in_person_products,
)
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def products_client(mock_ryft_client):
    return InPersonProductsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_products_list_default_params(products_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_products()
    resp = await products_client.list()
    mock_ryft_client.get.assert_called_once_with(
        "in-person/products",
        {"ascending": None, "limit": None, "startsAfter": None},
    )
    assert resp == mock_in_person_products()


@pytest.mark.asyncio
async def test_products_list_custom_params(products_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_products()
    resp = await products_client.list(
        ascending=True, limit=20, startsAfter="ippd_01FCTS1XMKH9FF43CAFA4CXT3P"
    )
    mock_ryft_client.get.assert_called_once_with(
        "in-person/products",
        {
            "ascending": True,
            "limit": 20,
            "startsAfter": "ippd_01FCTS1XMKH9FF43CAFA4CXT3P",
        },
    )
    assert resp == mock_in_person_products()


@pytest.mark.asyncio
async def test_products_list_error(products_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await products_client.list()
