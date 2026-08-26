import pytest
from eval_add import add

def test_add_positive_numbers():
    assert add(1, 2) == 3
    assert add(10, 20) == 30

def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert pytest.approx(add(0.1, 0.2)) == 0.3
