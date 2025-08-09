import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payment_methods import PaymentMethodsClient
from ryft_sdk.models.errors import RyftError
from ryft_sdk.models.payment_methods.req.payment_methods_req import (
    UpdatePaymentMethodRequest,
)
from typing import cast
from test.mock_error import mock_ryft_error
from test.payment_methods.mock_data.mock_payment_method_resp import (
    mock_payment_method_resp,
)
from test.payment_methods.mock_data.mock_update_payment_method_req import (
    mock_update_payment_method_req,
)

mock_payment_method_id = "pm_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payment_methods_client(mock_ryft_client):
    return PaymentMethodsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payment_methods_update(payment_methods_client, mock_ryft_client):
    mock_ryft_client.patch.return_value = mock_payment_method_resp()
    req = cast(UpdatePaymentMethodRequest, mock_update_payment_method_req())
    resp = await payment_methods_client.update(mock_payment_method_id, req)
    mock_ryft_client.patch.assert_called_once_with(
        f"payment-methods/{mock_payment_method_id}", req
    )
    assert resp == mock_payment_method_resp()


@pytest.mark.asyncio
async def test_payment_methods_update_error(payment_methods_client, mock_ryft_client):
    mock_ryft_client.patch.side_effect = mock_ryft_error()
    req = cast(UpdatePaymentMethodRequest, mock_update_payment_method_req())
    with pytest.raises(RyftError):
        await payment_methods_client.update(mock_payment_method_id, req)
