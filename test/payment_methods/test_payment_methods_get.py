from __future__ import annotations

import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_methods import PaymentMethodsClient
from ryft_sdk.models.errors import RyftError

from test.mock_error import mock_ryft_error
from test.payment_methods.mock_data.mock_payment_method_resp import (
    mock_payment_method_resp,
)

mock_payment_method_id = "pm_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payment_methods_client(mock_ryft_client):
    return PaymentMethodsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payment_methods_get(payment_methods_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_payment_method_resp()
    resp = await payment_methods_client.get(mock_payment_method_id)
    mock_ryft_client.get.assert_called_once_with(
        f"payment-methods/{mock_payment_method_id}"
    )
    assert resp == mock_payment_method_resp()


@pytest.mark.asyncio
async def test_payment_methods_get_error(payment_methods_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await payment_methods_client.get(mock_payment_method_id)
