def mock_in_person_location():
    return {
        "id": "iploc_01FCTS1XMKH9FF43CAFA4CXT3P",
        "name": "Ryft Computer Parts",
        "address": {
            "lineOne": "123 Street",
            "city": "Manchester",
            "country": "GB",
            "postalCode": "M1 1AA",
        },
        "geoCoordinates": {"latitude": 51.1789, "longitude": 1.8262},
        "metadata": {"custom": "12345"},
        "createdTimestamp": 1470989538,
        "lastUpdatedTimestamp": 1470989538,
    }


def mock_in_person_locations():
    return {
        "items": [mock_in_person_location()],
        "paginationToken": None,
    }


def mock_create_location_req():
    return {
        "name": "Ryft Computer Parts",
        "address": {
            "lineOne": "123 Street",
            "city": "Manchester",
            "country": "GB",
            "postalCode": "M1 1AA",
        },
        "geoCoordinates": {"latitude": 51.1789, "longitude": 1.8262},
        "metadata": {"custom": "12345"},
    }


def mock_update_location_req():
    return {
        "name": "Updated Location Name",
        "metadata": {"updated": "true"},
    }
