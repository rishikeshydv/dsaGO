from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        idx_list = []
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i - 1] and nums[i] == nums[i + 1]:
                idx_list.append(i)
        
        # Here, we shift the elements at these indices to the end of the list
        shift_count = 0
        for idx in idx_list:
            idx -= shift_count
            for i in range(idx, n - 1):
                nums[i] = nums[i + 1]
            shift_count += 1
            nums[n - shift_count] = '_'
        
        return n - shift_count

# Example usage:
sol = Solution()
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
new_length = sol.removeDuplicates(nums)
print("The new length of the array is:", new_length)
print("The modified array is:", nums[:new_length])
