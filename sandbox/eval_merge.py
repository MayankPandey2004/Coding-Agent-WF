def merge_sorted(arr1, arr2):
    """Merge two sorted lists into a single sorted list.

    Args:
        arr1 (list): First sorted list.
        arr2 (list): Second sorted list.

    Returns:
        list: Merged sorted list containing all elements from arr1 and arr2.
    """
    i, j = 0, 0
    merged = []
    # Iterate through both arrays until one is exhausted
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Append any remaining elements from arr1 or arr2
    if i < len(arr1):
        merged.extend(arr1[i:])
    if j < len(arr2):
        merged.extend(arr2[j:])
    return merged
