def maxProfit(prices):
    if(len(prices) < 2):
        return 0
    
    min_val = prices[0]
    max_profit = 0
    
    for i in prices:
        if i < min_val:
            min_val = i

        if i > min_val and max_profit < i-min_val:
            max_profit = i - min_val
            
        
    return max_profit

prices = [7,6,4,3,1]
print(maxProfit(prices))