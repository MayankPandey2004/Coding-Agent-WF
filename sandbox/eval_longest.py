def longest_substring_without_repeating(s: str) -> int:
    """Return the length of the longest substring without repeating characters.

    Uses a sliding window approach with a dictionary storing the most recent index
    of each character seen. The window is defined by ``start`` (inclusive) and the
    current index ``i`` (inclusive). When a repeated character is encountered, the
    ``start`` pointer jumps to one position after the previous occurrence, if that
    position is ahead of the current ``start``.

    Args:
        s: Input string.

    Returns:
        The maximum length of a substring of ``s`` that contains no duplicate
        characters. For an empty string the result is ``0``.
    """
    # Edge case: empty string
    if not s:
        return 0

    # Mapping from character to its latest index in the string.
    last_index: dict[str, int] = {}
    max_len = 0
    start = 0  # start index of current window

    for i, ch in enumerate(s):
        # If the character was seen and its last occurrence is within the current window
        if ch in last_index and last_index[ch] >= start:
            # Move start to one position after the previous occurrence
            start = last_index[ch] + 1
        # Update the last seen index for the character
        last_index[ch] = i
        # Update max length if the current window is larger
        current_len = i - start + 1
        if current_len > max_len:
            max_len = current_len

    return max_len
