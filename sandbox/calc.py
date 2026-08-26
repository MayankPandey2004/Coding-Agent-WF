class DivisionByZeroError(ValueError):
    """Custom exception for division by zero."""
    pass

def divide(a, b):
    """Return a divided by b.

    Raises:
        DivisionByZeroError: If b is zero.
    """
    if b == 0:
        raise DivisionByZeroError("cannot divide by zero")
    return a / b
