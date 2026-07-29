class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Go through array, initialize hash fgor O(1) lookups later
        # After initializing hash, check to see if i+1 already exist in hash
        # Then we call union on the two sets
        # If they do, add to disjoint set (union)
        # Use path compression to make calculating size more efficient
        # Then, we can go through and find the largest set and return the size

        numSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in numSet:
                curLength = 1
                while n + 1 in numSet:
                    curLength += 1
                    n += 1
                if curLength > longest:
                    longest = curLength
        
        return longest


