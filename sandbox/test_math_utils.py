import pytest
from math_utils import add

def test_add_integers():
    assert add(1, 2) == 3
    assert add(-1, 5) == 4

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_add_strings():
    assert add('a', 'b') == 'ab'
