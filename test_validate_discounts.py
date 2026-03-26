import pytest
from discounts import apply_discounts

# Base cart total for testing
cart_total = 100.0

@pytest.mark.parametrize("codes, expected_total, use_approx, expect_error", [
    (['SAVE10'], 90.0, False, False),                     # Single valid discount
    (['SAVE20'], 80.0, False, False),                     # Single valid discount
    (['SAVE10', 'SAVE20'], 70.0, False, False),           # Multiple valid discounts
    (['SAVE50', 'SAVE20'], 30.0, True, False),            # Multiple valid discounts (float approx)
    (['SAVE50', 'SAVE50', 'SAVE10'], None, False, True),  # Overlapping discount > 100%, 50 + 50 = Free?? is possible
                                                         # due to checker being ≥1 and not >=1,
    (['SAVE10', 'INVALID'], None, False, True),           # Invalid discount code
    ([], 100.0, False, False),                            # No discounts
])

def test_apply_discounts(codes, expected_total, use_approx, expect_error):
    if expect_error:
        # Expect ValueError for invalid or overlapping discounts
        with pytest.raises(ValueError):
            apply_discounts(cart_total, codes)
        print(f"{codes} failed (as it should)")
    else:
        total = apply_discounts(cart_total, codes)
        print(f"Codes {codes} -> final total: {total}, expected: {expected_total}")
        # approx for rounding
        if use_approx:
            assert total == pytest.approx(expected_total)
        else:
            assert total == expected_total
