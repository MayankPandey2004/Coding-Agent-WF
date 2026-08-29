def reverse_words(s: str) -> str:
    """Return a new string with the order of words reversed.

    The function splits the input string on whitespace, reverses the list of
    words, and joins them back together with a single space. Leading and trailing
    whitespace is stripped, and any amount of internal whitespace is treated as a
    separator.

    Args:
        s: The input sentence.

    Returns:
        A string with the words in reverse order.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Split on any whitespace, filter out empty strings (in case of multiple spaces)
    words = s.split()
    reversed_words = list(reversed(words))
    return " ".join(reversed_words)
