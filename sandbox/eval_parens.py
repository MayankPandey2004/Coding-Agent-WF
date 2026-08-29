def is_valid(s: str) -> bool:
    """Check if the brackets in the string are balanced and correctly nested.

    Supports parentheses ``()``, square brackets ``[]`` and curly braces ``{}``.
    Any other characters are ignored.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Mapping of closing to opening brackets
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())
    stack: list[str] = []

    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        # ignore other characters

    return not stack
