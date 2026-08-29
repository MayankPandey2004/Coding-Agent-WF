def are_anagrams(s1: str, s2: str) -> bool:
    """Return True if *s1* and *s2* are anagrams of each other.

    The comparison is case‑sensitive and includes all characters (including
    whitespace and punctuation). If either argument is not a string, a
    ``TypeError`` is raised.
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both arguments must be strings")
    # Quick length check
    if len(s1) != len(s2):
        return False
    # Compare sorted characters
    return sorted(s1) == sorted(s2)
