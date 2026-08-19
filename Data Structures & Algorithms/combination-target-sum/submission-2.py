class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtrack(index, cur, total):
            if index >= len(nums) or total > target:
                return

            if total == target:
                ret.append(cur.copy())
                return
            
            cur.append(nums[index])
            backtrack(index, cur, total + nums[index])
            
            cur.pop()
            backtrack(index + 1, cur, total)

        backtrack(0, [], 0)
        return ret
