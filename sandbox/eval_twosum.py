def two_sum(nums, target):
    """Return indices of the two numbers in `nums` that add up to `target`.

    Args:
        nums (list[int]): List of integers.
        target (int): The target sum.

    Returns:
        list[int]: A list containing the two indices. If no such pair exists,
            returns an empty list.

    The function uses a hash map to achieve O(n) time complexity.
    """
    # Dictionary to store number -> its index
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    # If no solution found, return empty list (could also raise an error)
    return []
