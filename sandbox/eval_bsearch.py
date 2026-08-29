# eval_bsearch.py
"""
Binary search implementation.

Provides a function `binary_search(arr, target)` that searches for `target` in a sorted
list `arr` using the binary search algorithm. If the target is found, the index of the
target is returned; otherwise, -1 is returned.

The function validates that the input `arr` is a sequence (list or tuple) and that
its elements are comparable with `target`. It does not modify the input array.
"""

from typing import Sequence, Any


def binary_search(arr: Sequence[Any], target: Any) -> int:
    """Perform binary search on a sorted sequence.

    Args:
        arr: A sorted sequence (e.g., list or tuple) of comparable items.
        target: The value to search for.

    Returns:
        The index of ``target`` in ``arr`` if present; otherwise ``-1``.
    """
    if not isinstance(arr, (list, tuple)):
        raise TypeError("arr must be a list or tuple")

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Simple manual test (executed only when run directly)
if __name__ == "__main__":
    test_arr = [1, 3, 5, 7, 9, 11]
    for t in [5, 6, 11, -1]:
        print(f"search {t} -> {binary_search(test_arr, t)}")
