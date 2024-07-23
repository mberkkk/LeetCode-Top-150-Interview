def maxProfit( prices):
    if len(prices) < 2:
        return 0
    
    current_min_val = prices[0]
    max_profit = 0
    index = 0
    sep_profit = 0
    
    for i in range(len(prices)-1):
        if (prices[i+1] - prices [i] > 0):
            max_profit += prices [i+1] - prices[i]
    
    return max_profit
    
prices = [5,4,8,3,1,9]
print(maxProfit(prices=prices))