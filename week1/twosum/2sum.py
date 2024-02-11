from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in indices:
            return [indices[complement], i]
        else:
            indices[num] = i
    return []

print(twoSum([1, 2, 3], 5))
