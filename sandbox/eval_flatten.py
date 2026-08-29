def flatten(nested_list):
    """Recursively flatten a nested list.

    Args:
        nested_list (list): A list which may contain other lists as elements.

    Returns:
        list: A new list containing all the non-list elements from ``nested_list``
            in a single, flat sequence.
    """
    flat = []
    for element in nested_list:
        if isinstance(element, list):
            flat.extend(flatten(element))
        else:
            flat.append(element)
    return flat
