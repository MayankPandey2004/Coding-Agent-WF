import pytest
from math_utils import add

def test_add_integers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_floats():
    assert add(2.5, 3.1) == pytest.approx(5.6)

def test_add_strings():
    assert add('a', 'b') == 'ab'
