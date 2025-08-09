def mock_platform_fee_resp():
    return {
        "id": "pf_01FCTS1XMKH9FF43CAFA4CXT3P",
        "paymentSessionId": "ps_01JJPPAZTNN38EMDJ72FASHE7R",
        "amount": 40,
        "paymentAmount": 450,
        "processingFee": 7,
        "netAmount": 33,
        "currency": "GBP",
        "fromAccountId": "ac_b83f2653-06d7-44a9-a548-5825e8186004",
        "createdTimestamp": 1470989538,
    }


def mock_platform_fees_resp():
    return {
        "items": [mock_platform_fee_resp()],
    }
