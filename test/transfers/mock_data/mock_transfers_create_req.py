def mock_create_transfer_req_send_to_sub_account():
    return {
        "amount": 1500,
        "currency": "GBP",
        "destination": {"accountId": "ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327"},
        "reason": "Money owed from payments on 2012-01-30",
    }


def mock_create_transfer_req_pull_money_from_sub_account():
    return {
        "amount": 1500,
        "currency": "GBP",
        "source": {"accountId": "ac_3fe8398f-8cdb-43a3-9be2-806c4f84c327"},
        "reason": "Dispute Fees",
    }
