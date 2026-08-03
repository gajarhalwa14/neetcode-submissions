class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] == target: return m
            if nums[m] < target:
                if nums[l] <= nums[m] or target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # nums[m] > target
                if nums[r] >= nums[m] or target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1

                


            
        return -1