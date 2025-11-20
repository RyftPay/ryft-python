from __future__ import annotations

import pytest
from unittest.mock import Mock

from ryft_sdk.client import RyftClient
from ryft_sdk.clients.in_person_orders import InPersonOrdersClient
from ryft_sdk.models.errors import RyftError
from test.in_person_orders.mock_data.mock_order_resp import mock_in_person_order
from test.mock_error import mock_ryft_error


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def orders_client(mock_ryft_client):
    return InPersonOrdersClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_orders_get(orders_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_order()
    resp = await orders_client.get("ipord_01FCTS1XMKH9FF43CAFA4CXT3P")
    mock_ryft_client.get.assert_called_once_with(
        "in-person/orders/ipord_01FCTS1XMKH9FF43CAFA4CXT3P", account=None
    )
    assert resp == mock_in_person_order()


@pytest.mark.asyncio
async def test_orders_get_with_account(orders_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_in_person_order()
    resp = await orders_client.get(
        "ipord_01FCTS1XMKH9FF43CAFA4CXT3P",
        account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327",
    )
    mock_ryft_client.get.assert_called_once_with(
        "in-person/orders/ipord_01FCTS1XMKH9FF43CAFA4CXT3P",
        account="ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327",
    )
    assert resp == mock_in_person_order()


@pytest.mark.asyncio
async def test_orders_get_error(orders_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await orders_client.get("ipord_01FCTS1XMKH9FF43CAFA4CXT3P")
