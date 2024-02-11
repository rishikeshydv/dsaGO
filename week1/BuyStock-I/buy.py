class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            buy = min(buy,prices[i])
            maxProfit = max(maxProfit,prices[i]-buy)
            
        return maxProfit

sol = Solution()
print(f"Your Profit is {sol.maxProfit([7,6,4,3,1])}")
        