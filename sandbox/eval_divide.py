def safe_divide(a, b):
    """Return a / b, raising ValueError if b is zero.

    Args:
        a: Numerator (int, float, or any type supporting division).
        b: Denominator.

    Raises:
        ValueError: If b == 0.
    """
    if b == 0:
        raise ValueError('cannot divide by zero')
    return a / b
