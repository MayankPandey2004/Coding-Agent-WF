def factorial(n: int) -> int:
    """Return the factorial of a non‑negative integer n using recursion.

    Args:
        n (int): Non‑negative integer for which to compute the factorial.

    Returns:
        int: The factorial of n (n!).

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("factorial() only accepts integer arguments")
    if n < 0:
        raise ValueError("factorial() not defined for negative integers")
    if n == 0:
        return 1
    return n * factorial(n - 1)
