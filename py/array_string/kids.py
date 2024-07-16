#1431. Kids With the Greatest Number of Candies
'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
'''
from typing import List
def kids(candiesList:List[int], extraCandies:int):
    if not candiesList:
        return
    l=0
    r=len(candiesList)-1
    maxVal = 0
    res = [False]*len(candiesList)
    #retrieving the max value in a list
    while l<=r:
        if candiesList[l]>=candiesList[r]:
            maxVal = candiesList[l]
        else:
            maxVal = candiesList[r]
    #main job
    l=0
    r=len(candiesList)-1
    while l<=r:
        if candiesList[l]+extraCandies >= maxVal:
            res[l]=True
            l+=1
        if candiesList[r]+extraCandies >= maxVal:
            res[r]=True
            r+=1
    return res

#test
candies = [2,3,5,1,3]
extraCandies = 3

print(kids(candies,extraCandies))