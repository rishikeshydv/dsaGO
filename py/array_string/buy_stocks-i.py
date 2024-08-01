def maxProfit(prices):
    profit = 0
    buy = 999999999999
    for i in range(len(prices)):
        buy = min(prices[i],buy)
        profit = max(profit,prices[i]-buy)
    return profit

print(maxProfit([7,6,4,3,1]))
