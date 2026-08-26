def safe_divide(a, b):
    """Return a divided by b, raising a ValueError if b is zero.

    Args:
        a (numeric): Numerator.
        b (numeric): Denominator.

    Returns:
        numeric: The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError('cannot divide by zero')
    return a / b
