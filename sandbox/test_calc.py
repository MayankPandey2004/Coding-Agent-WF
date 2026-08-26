import pytest
from calc import divide, DivisionByZeroError

def test_normal_division():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError) as exc_info:
        divide(5, 0)
    assert str(exc_info.value) == "cannot divide by zero"
