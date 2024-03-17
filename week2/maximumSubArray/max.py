#Given an integer array nums, find the subarray with the largest sum, and return the subarray & its sum.

from typing import List
class Solution:
    def __init__(self):
        self.currSum = 0
        self.currList = []
        self.maxDict = {}
    def maxSubArray(self, nums: List[int]):
        for i in range(0,len(nums),1):
            if self.currSum>=0:
                if self.currSum <= (self.currSum+sum(nums[i:])):
                    self.currSum += nums[i]
                    self.currList.append(nums[i])
                else:
                    if sum(self.currList) in self.maxDict.keys():
                        self.maxDict[sum(self.currList)].append(self.currList)
                    else:
                        self.maxDict[sum(self.currList)] = self.currList
            else:
                self.currSum = 0
                self.currList = []
                
        maxSum = max(self.maxDict.keys())
        return (maxSum,self.maxDict[maxSum])
    

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
                
                
            
        