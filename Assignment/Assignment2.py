def max_subarray_sum(nums):
    """
    Find the maximum sum of a subarray in the given array.

    Args:
    nums (List[int]): List of integers.

    Returns:
    int: The sum of the subarray with the largest sum.
    """
    # Initialize max_now and max_general with the first element
    max_now = max_general = nums[0]

    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Updating max_now to either the current number or the current number + max_now
        max_now = max(num, max_now + num)

        # Updating max_general if max_now is greater
        max_general = max(max_general, max_now)

    return max_general

