from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.conversions import ConversionsClient
from ryft_sdk.models.errors import RyftError
from test.mock_error import mock_ryft_error
from test.conversions.mock_data.mock_conversions_resp import mock_conversion_resp

mock_conversion_id = "con_01FCTS1XMKH9FF43CAFA4CXT3P"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def conversions_client(mock_ryft_client):
    return ConversionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_conversions_get(conversions_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_conversion_resp()
    resp = await conversions_client.get(mock_conversion_id)
    mock_ryft_client.get.assert_called_once_with(f"conversions/{mock_conversion_id}")
    assert resp == mock_conversion_resp()


@pytest.mark.asyncio
async def test_conversions_get_error(conversions_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await conversions_client.get(mock_conversion_id)
