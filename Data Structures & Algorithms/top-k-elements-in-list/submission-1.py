class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use dict/hash to count and store occurences
        # Use heap to store max heap sorted by occurences
        # With tuple (value, # occurrences), # occurrences being the key

        # initialize dict with occurences, O(n) time
        numsDict = (Counter(nums))

        numsTuples = [(count, num) for num, count in numsDict.items()]

        heapq.heapify_max(numsTuples)
        retArr = []
        for _ in range(k):
            occurrences, num = heapq.heappop_max(numsTuples)
            retArr.append(num)
        
        return retArr

