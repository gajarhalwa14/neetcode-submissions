class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = math.sqrt(point[0] * point[0] + (point[1] * point[1]))
            distances.append((distance, point))

        heapq.heapify_max(distances)

        while len(distances) > k:
            heapq.heappop_max(distances)

        ret = [distance[1] for distance in distances]

        return ret

        