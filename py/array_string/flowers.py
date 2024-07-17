#605. Can Place Flowers
'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False
        if n == 0:
            return True
        
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or if it's the first/last plot
                empty_prev = (i == 0 or flowerbed[i - 1] == 0)
                empty_next = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if empty_prev and empty_next:
                    # Plant a flower here
                    flowerbed[i] = 1
                    n -= 1
                    # If all required flowers are planted, return True
                    if n == 0:
                        return True
                    # Skip the next plot since we just planted a flower here
                    i += 1

        return n == 0

        
        