def reverse_words(s: str) -> str:
    """Return a new string with the order of words reversed.

    Args:
        s: Input sentence string. Words are assumed to be separated by whitespace.
    Returns:
        A string with the words in reverse order, preserving the original spacing
        between words as a single space. Leading/trailing whitespace is stripped.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Split on whitespace to get words, then reverse and join with a single space.
    words = s.split()
    return " ".join(reversed(words))
