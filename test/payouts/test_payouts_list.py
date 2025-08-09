import pytest
from unittest.mock import Mock
from ryft_sdk.client import RyftClient
from ryft_sdk.clients.payouts import PayoutsClient
from ryft_sdk.models.errors import RyftError
from test.accounts.mock_data.mock_payout_resp import mock_payouts_resp
from test.mock_error import mock_ryft_error

mock_account_id = "acc_123"


@pytest.fixture
def mock_ryft_client():
    return Mock(spec=RyftClient)


@pytest.fixture
def payouts_client(mock_ryft_client):
    return PayoutsClient(mock_ryft_client)


@pytest.mark.asyncio
async def test_payouts_list_with_defaults(payouts_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_payouts_resp()
    resp = await payouts_client.list(mock_account_id)
    mock_ryft_client.get.assert_called_once_with(
        f"accounts/{mock_account_id}/payouts",
        {
            "startTimestamp": None,
            "endTimestamp": None,
            "ascending": None,
            "limit": None,
            "startsAfter": None,
        },
    )
    assert resp == mock_payouts_resp()


@pytest.mark.asyncio
async def test_payouts_list_with_custom_params(payouts_client, mock_ryft_client):
    mock_ryft_client.get.return_value = mock_payouts_resp()
    resp = await payouts_client.list(
        mock_account_id,
        startTimestamp=1234567890,
        endTimestamp=1234567891,
        ascending=True,
        limit=10,
        startsAfter="foo",
    )
    mock_ryft_client.get.assert_called_once_with(
        f"accounts/{mock_account_id}/payouts",
        {
            "startTimestamp": 1234567890,
            "endTimestamp": 1234567891,
            "ascending": True,
            "limit": 10,
            "startsAfter": "foo",
        },
    )
    assert resp == mock_payouts_resp()


@pytest.mark.asyncio
async def test_payouts_list_error(payouts_client, mock_ryft_client):
    mock_ryft_client.get.side_effect = mock_ryft_error()
    with pytest.raises(RyftError):
        await payouts_client.list(mock_account_id)
