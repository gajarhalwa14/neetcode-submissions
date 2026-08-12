class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first_stone = heapq.heappop_max(stones)
            second_stone = heapq.heappop_max(stones)

            if first_stone == second_stone:
                continue

            if first_stone > second_stone:
                first_stone -= second_stone
                heapq.heappush_max(stones, first_stone)
            else:
                second_stone -= first_stone
                heapq.heappush_max(stones, second_stone)
        if len(stones) == 0: return 0
        return stones[0]

