class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Two pointer l, r
    # If l > r, shift l to r
    # [5, 12, 19, 6, 14, 7, 10, 11, 13, 10, 14, 20]

        l, r, ret = 0, 1, 0
        while r < len(prices):
            if l == r:
                r += 1
                continue
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            else:
                profit = prices[r] - prices[l]
                if profit > ret:
                    ret = profit
                r += 1
        
        return ret

        