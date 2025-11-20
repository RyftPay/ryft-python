from __future__ import annotations


def mock_apple_pay_domain_resp():
    return {
        "id": "ap_123",
        "domainName": "https://domain.test",
        "createdTimestamp": 776170800,
    }


def mock_apple_pay_domains_resp():
    return {
        "items": [mock_apple_pay_domain_resp()],
        "paginationToken": "",
    }
