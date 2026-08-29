def dedupe_preserve_order(lst):
    """Return a new list with duplicates removed while preserving the original order.

    Parameters
    ----------
    lst : list
        The input list from which to remove duplicate items.

    Returns
    -------
    list
        A list containing the first occurrence of each element in ``lst``.

    Examples
    --------
    >>> dedupe_preserve_order([1, 2, 3, 2, 1, 4])
    [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
