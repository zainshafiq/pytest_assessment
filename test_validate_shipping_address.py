import pytest
from shipping_address import validate_shipping_address

# Sample addresses
valid_address = {
    'name': 'Mr Loba Loba',
    'street': 'Backstreet Guy',
    'city': 'Kuala Lumpur',
    'postcode': '50000',
    'country': 'Malaysia'
}

missing_name = {
    'street': 'Jalan Bukit Bintang',
    'city': 'JB',
    'postcode': '50000',
    'country': 'Malaysia'
}

missing_city_post = {
    'name': 'Mr. Bombastic',
    'street': 'Jalan 2',
    'country': 'Malaysia'
}

not_dict = ['not', 'a', 'dict']

@pytest.mark.parametrize("address, expect_ok", [
    (valid_address, True),        # Valid address
    (missing_name, False),        # Missing name
    (missing_city_post, False),   # Missing city & postcode
    ({}, False),                 # Empty dict
    (not_dict, False),           # Non-dict input
])

def test_address(address, expect_ok):
    if expect_ok:
        assert validate_shipping_address(address) is True
        print(f"{address} passed")
    # Expect ValueError for invalid addresses
    else:
        with pytest.raises(ValueError):
            validate_shipping_address(address)
        print(f"{address} failed (as it should)")
