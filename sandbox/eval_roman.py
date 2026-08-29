def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to its integer value.

    The function supports standard Roman numerals using the symbols:
    I (1), V (5), X (10), L (50), C (100), D (500), M (1000).
    It also correctly handles subtractive notation such as IV (4), IX (9),
    XL (40), XC (90), CD (400) and CM (900).

    Parameters
    ----------
    s: str
        Roman numeral string. The function is case‑insensitive and will
        ignore surrounding whitespace.

    Returns
    -------
    int
        The integer representation of the Roman numeral.

    Raises
    ------
    ValueError
        If the input contains characters that are not valid Roman numerals.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    s = s.strip().upper()
    if not s:
        raise ValueError("Empty Roman numeral string")

    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    # Validate characters
    for ch in s:
        if ch not in roman_map:
            raise ValueError(f"Invalid Roman numeral character: {ch}")

    total = 0
    i = 0
    while i < len(s):
        # Look ahead to see if we have a subtractive pair
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            total += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            total += roman_map[s[i]]
            i += 1
    return total
