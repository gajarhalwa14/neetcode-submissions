class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

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


