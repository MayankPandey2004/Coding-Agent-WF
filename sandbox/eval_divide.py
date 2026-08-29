def safe_divide(a, b):
    """Return a divided by b, raising ValueError if b is zero.

    Args:
        a: Numerator (int or float).
        b: Denominator (int or float).
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError('cannot divide by zero')
    return a / b
