class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profit = 0

        for p in prices:
            min_buy = min(min_buy, p)
            profit = max(profit, p - min_buy)

        return profit 
        