class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # minStock = prices[0]
        # bestG = 0

        # for i in range(1, n):
        #     if prices[i] <= minStock :
        #         minStock = prices[i]

        #     else :
        #         bestG = max(bestG, prices[i] - minStock)

        # return bestG 
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
        