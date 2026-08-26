def is_even(n: int) -> bool:
    """Return True if the given integer n is even, False otherwise.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is even, False if n is odd.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n % 2 == 0
