class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            # if r - l == 1: return min(nums[l], nums[r])
            m = (r - l) // 2 + l
            if nums[m-1] > nums[m]: return nums[m] 
            if nums[m] < nums[r] or nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1

        return nums[l]