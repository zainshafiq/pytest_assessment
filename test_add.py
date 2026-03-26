import pytest
from add import add

@pytest.mark.parametrize("a,b,expected_num,use_approx", [
    (2,3,5, False),            # positive numbers
    (-2,3,1, False),           # mixed numbers
    (0,0,0, False),            # both zero
    (0,5,5, False),            # zero + positive
    (-1,-2,-3, False),         # negative numbers
    (1.0,1.5,2.5, True),       # float
    (0.1,1.9,2.0, True),       # float
    (0.1,0.2,0.3, True),       # float edge case, result = 0.30000000000000004, will fail if dont use approx
    (0.3,0.6,0.9, True),       # float edge case, result = 0.8999999999999999, will fail if dont use approx
])

def test_add(a,b,expected_num,use_approx):
    # Print
    # print(f"{a} + {b} = {add(a,b)}, expected {expected_num}")

    # If float cases, use approx for rounding
    if use_approx:
        assert add(a,b) == pytest.approx(expected_num)
    # If not, use normal assert
    else:
        assert add(a,b) == expected_num
