def factorial(n: int) -> int:
    """Return the factorial of a non‑negative integer n using recursion.

    Args:
        n (int): A non‑negative integer. ``0`` returns ``1``.

    Returns:
        int: The factorial of ``n``.

    Raises:
        ValueError: If ``n`` is negative.
        TypeError: If ``n`` is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non‑negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)
