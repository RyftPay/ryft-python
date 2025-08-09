def mock_continue_payment_req_submit_3ds_fingerprint_result():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "threeDs": {
            "fingerprint": "ewogICJ0aHJlZURTU2VydmVyVHJhbnNJRCI6ICI4ZjAxNzdhNC0yY2VkLTQ4NjUtODViNy1iYWQ5YmZhMzk4ZDIiLAogICJ0aHJlZURTQ29tcEluZCI6IlkiCn0="
        },
    }


def mock_continue_payment_req_submit_3ds_challenge_result():
    return {
        "clientSecret": "ps_01FCTS1XMKH9FF43CAFA4CXT3P_secret_b83f2653-06d7-44a9-a548-5825e8186004",
        "threeDs": {"challengeResult": "ewogICJ0cmFuc1N0YXR1cyI6IlkiCn0="},
    }
