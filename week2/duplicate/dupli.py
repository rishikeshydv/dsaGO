from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for n in  nums:
            if n in numDict.keys():
                return True
            else:
                numDict[n]=1        
        return False
    
sol = Solution()
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    
    
        