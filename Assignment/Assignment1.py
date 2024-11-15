def two_sum(nums, target):
    """
    Find two indices in an array such that the values at these indices sum up to a target.

    Args:
    nums (List[int]): Input array of integers.
    target (int): Target sum.

    Returns:
    List[int]: The indices of the two numbers that add up to the target.
               If no solution is found, an empty list is returned.
    """
    # Dictionary to store the numbers seen and their indices
    num_to_be_indexed = {}

    # Loop through each number in the array
    for j, num in enumerate(nums):
        # Calculate the complemented that would add up to the target
        complemented = target - num

        # Check if the complemented exists in the dictionary
        if complemented in num_to_be_indexed:
            # If complemented exists, return the indices
            return [num_to_be_indexed[complemented], j]

        # Otherwise, add the current number with its index to the dictionary
        num_to_be_indexed[num] = j

    # Return an empty list if no solution is found
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
