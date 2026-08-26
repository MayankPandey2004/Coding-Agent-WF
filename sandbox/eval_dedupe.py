def dedupe_preserve_order(lst):
    """Return a new list with duplicates removed while preserving the original order.

    Args:
        lst (list): The input list which may contain duplicate elements.

    Returns:
        list: A list containing the first occurrence of each element from ``lst``.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
