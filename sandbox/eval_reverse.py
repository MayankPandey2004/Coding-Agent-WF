def reverse_words(s: str) -> str:
    """Return a new string with the order of words reversed.

    The function splits the input string on whitespace, reverses the list of
    words, and joins them back together with a single space. It preserves the
    original spacing only insofar as words are separated by a single space in the
    output.

    Args:
        s: The input sentence.

    Returns:
        A sentence with the word order reversed.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Split on whitespace to get words, ignoring extra spaces
    words = s.split()
    # Reverse the list of words and join with a single space
    return " ".join(reversed(words))
