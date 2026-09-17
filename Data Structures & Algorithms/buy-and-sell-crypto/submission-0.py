class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best, min_price = 0, prices[0]
        for p in prices:
            min_price, best = min(min_price, p), max(best, p - min_price)
        return best