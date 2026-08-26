def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s == s[::-1]
