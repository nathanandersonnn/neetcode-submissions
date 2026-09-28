class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best, min_price = 0, prices[0]
        for price in prices:
            best, min_price = max(best, price - min_price), min(min_price, price)
        return best