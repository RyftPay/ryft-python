from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.conversions import ConversionsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.conversions.req.conversions_req import CreateConversionRequest
from typing import cast

from test.mock_error import mock_ryft_error
from test.conversions.mock_data.mock_conversions_create_req import (
    mock_create_conversion_req,
)
from test.conversions.mock_data.mock_conversions_resp import mock_conversion_resp


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def conversions_client(mock_ryft_client):
    return ConversionsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_conversions_create(conversions_client, mock_ryft_client):
    mock_ryft_client.post.return_value = mock_conversion_resp()
    req = cast(CreateConversionRequest, mock_create_conversion_req())
    resp = await conversions_client.create(req)
    mock_ryft_client.post.assert_called_once_with("conversions", req)
    assert resp == mock_conversion_resp()


@pytest.mark.asyncio
async def test_conversions_create_error(conversions_client, mock_ryft_client):
    mock_ryft_client.post.side_effect = mock_ryft_error()
    req = cast(CreateConversionRequest, mock_create_conversion_req())
    with pytest.raises(RyftError):
        await conversions_client.create(req)
