class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update the lowest price we've encountered so far
            if price < min_price:
                min_price = price
            # Otherwise, calculate profit if we sold today and update max_profit
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)

        return max_profit
                    

            