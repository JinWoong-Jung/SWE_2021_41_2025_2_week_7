from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]

# Example 1:
print('Example 1:', twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
# Example 2:
print('Example 2:', twoSum([3, 2, 4], 6))  # Output: [1, 2]
# Example 3:
print('Example 3:', twoSum([3, 3], 6))  # Output: [0, 1]