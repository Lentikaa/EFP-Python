def four_sum(nums, target):
    """
    Find all unique quadruplets in the array that sum up to the target.

    Args:
    nums (List[int]): The array of integers.
    target (int): The target sum for the quadruplets.

    Returns:
    List[List[int]]: A list of unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
                     nums[a] + nums[b] + nums[c] + nums[d] == target.
    """
    nums.sort()  # Sort the array to handle duplicates easily
    m = len(nums)
    result = []

    # Iterate through each element with two nested loops to fix the first two elements of the quadruplet
    for j in range(m - 3):
        # Skip duplicate values for j
        if j > 0 and nums[j] == nums[j - 1]:
            continue

        for k in range(j + 1, m - 2):
            # Skip duplicate values for k
            if k > j + 1 and nums[k] == nums[k - 1]:
                continue

            # Initialize two pointers for the remaining two elements of the quadruplet
            left, right = k + 1, m - 1

            while left < right:
                current_sum = nums[j] + nums[k] + nums[left] + nums[right]

                if current_sum == target:
                    # Add the quadruplet to the result if the sum matches the target
                    result.append([nums[j], nums[k], nums[left], nums[right]])

                    # Move left and right pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                # Adjust pointers based on the current sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result

# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums, target))
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
