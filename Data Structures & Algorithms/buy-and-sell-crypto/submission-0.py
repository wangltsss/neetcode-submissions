class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 101
        profit = 0
        for i in prices:
            if i - buy > profit:
                profit = i - buy
            if buy >= i:
                buy = i
        return profit