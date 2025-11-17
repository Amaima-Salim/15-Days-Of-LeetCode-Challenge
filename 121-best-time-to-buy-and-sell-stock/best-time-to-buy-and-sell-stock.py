class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            min_price=min(min_price,p)
            profit_today = p - min_price

            max_profit=max(profit_today,max_profit)

        return max_profit
        