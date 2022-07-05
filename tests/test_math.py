# test functions

import pytest


# first test
@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2

# failing test
@pytest.mark.math
def test_one_plus_two():
    a = 0
    b = 1
    c = 2  # make fail test
    assert a + b == c

# test with exception
@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)


# parameterised test
"""
def test_multiply_two_positive_ints():
    assert 2 * 3 == 6

def test_multiply_identity():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0
"""

products = {
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
}

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product