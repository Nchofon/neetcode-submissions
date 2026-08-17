class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minStock = prices[0]
        bestG = 0

        for i in range(1, n):
            if prices[i] <= minStock :
                minStock = prices[i]

            else :
                bestG = max(bestG, prices[i] - minStock)

        return bestG 
        