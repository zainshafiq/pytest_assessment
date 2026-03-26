import pytest
from cart import calculate_cart_total

# Sample carts
cart_normal = [{'price': 10, 'quantity': 2}, {'price': 5, 'quantity': 1}]        # total 25
cart_float_single = [{'price': 0.1, 'quantity': 1}, {'price': 0.2, 'quantity': 2}]  # total 0.5
cart_float_double = [{'price': 1.99, 'quantity': 1}, {'price': 25.99, 'quantity': 1}] # total 27.98

@pytest.mark.parametrize(
    "cart, discount, expected, use_approx",
    [
        (cart_normal, 0, 25, False),             # Normal case
        (cart_normal, 0.1, 22.5, True),          # Discount
        (cart_float_single, 0, 0.5, True),       # Float
        (cart_float_double, 0, 27.98, True),     # Float
        (cart_float_double, 0.2, 19.99, True),   # Float with 20% discount
        ([], 0, 0, False),                       # Empty cart
    ]
)

def test_calculate_cart_total(cart, discount, expected, use_approx):
    result = calculate_cart_total(cart, discount)
    print(f"Cart: {cart}, discount: {discount} -> total: {result}, expected: {expected}")

    # If float cases, use approx for rounding
    if use_approx:
        assert result == pytest.approx(expected)
    # If not, use normal assert
    else:
        assert result == expected


# Simple test for invalid inputs
@pytest.mark.parametrize(
    "bad_input",
    [
        None,
        123,
        "not a list",
        [1,2,3],
    ]
)
def test_calculate_cart_total_invalid(bad_input):
    print(f"Testing invalid input: {bad_input}")
    with pytest.raises(ValueError):
        calculate_cart_total(bad_input)
