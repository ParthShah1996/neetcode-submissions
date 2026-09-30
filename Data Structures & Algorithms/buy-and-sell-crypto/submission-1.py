class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 0
        profit = 0
        prices_length = len(prices)

        for i in range(prices_length):
            j = i + 1
            while j > i and j < prices_length: 
                profit = max(prices[j] - prices[i], profit)
                j += 1
        
        return profit
                

        