import pytest
from math_utils import subtract, multiply, divide, power

def test_subtract_positive():
    assert subtract(5, 3) == 2
    assert subtract(10, 0) == 10

def test_subtract_negative():
    assert subtract(3, 5) == -2
    assert subtract(-1, -1) == 0

def test_multiply_basic():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0

def test_multiply_commutative():
    a, b = 7, 9
    assert multiply(a, b) == multiply(b, a)

def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power_basic():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 1) == 3
    assert power(2, -2) == 0.25
