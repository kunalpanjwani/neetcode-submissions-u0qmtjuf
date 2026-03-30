class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []

        for i in range(len(prices)):
            if i == 0:
                continue
            
            sell_price = prices[i]
            m = min(prices[:i])
            if m > sell_price:
                continue
            else:
                profits.append(sell_price - m)
        return max(profits) if profits else 0
