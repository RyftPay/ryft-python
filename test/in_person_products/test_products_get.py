from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_products import InPersonProductsClient
from ryft_sdk.models.errors import RyftError
from test.in_person_products.mock_data.mock_product_resp import (
    mock_in_person_product,
)
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def products_client(mock_ryft_client):
    return InPersonProductsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_products_get(products_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_product()
    resp = await products_client.get("ippd_01FCTS1XMKH9FF43CAFA4CXT3P")
    mock_ryft_client.get.assert_called_once_with(
        "in-person/products/ippd_01FCTS1XMKH9FF43CAFA4CXT3P"
    )
    assert resp == mock_in_person_product()


@pytest.mark.asyncio
async def test_products_get_error(products_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await products_client.get("ippd_01FCTS1XMKH9FF43CAFA4CXT3P")
