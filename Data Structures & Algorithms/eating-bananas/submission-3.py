class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        m = max(piles)

        l, r = 1, m

        res = r

        while l <= r:
            k = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            if time <= h:
                res = min(res, k)
                r = k - 1
            elif time > h:
                l = k + 1

        return res   


