class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use dict/hash to count and store occurences
        # Use heap to store max heap sorted by occurences
        # With tuple (value, # occurrences), # occurrences being the key
        # Time complexity: O(n + klog(n))

        # initialize dict with occurences, O(n) time
        # numsDict = (Counter(nums))

        # numsTuples = [(count, num) for num, count in Counter(nums).items()]

        # heapq.heapify_max(numsTuples)
        # retArr = []
        # for _ in range(k):
        #     occurrences, num = heapq.heappop_max(numsTuples)
        #     retArr.append(num)
        
        # return retArr

        # Most effective approach - use bucket sort
        # Get dict like before, but create bucket indexes based on occurrences
        # We know that the number of buckets is dependent on the length of the input array
        # Because in worst case scenario, all numbers in the input array are the same
        # Meaning that there are n occurrences

        numsDict = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, count in numsDict.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result




