def is_palindrome(s: str) -> bool:
    """Return True if the given string is a palindrome, ignoring spaces and case.

    Parameters
    ----------
    s: str
        Input string to evaluate.

    Returns
    -------
    bool
        True if `s` is a palindrome when spaces are removed and case is ignored.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Normalize: remove spaces, convert to lower case
    normalized = ''.join(ch.lower() for ch in s if not ch.isspace())
    return normalized == normalized[::-1]
