def maxProfit(prices):
    profit = 0
    buy = 999999999
    for i in range(len(prices)):
        buy = min(buy,prices[i])
        if prices[i] > buy:
            profit += prices[i] - buy
            buy = prices[i]
    return profit

print(maxProfit([7,1,5,3,6,4]))