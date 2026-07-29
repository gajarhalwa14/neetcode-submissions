class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## NAIVE SOLUTION
        ## Two pointers i and j, iterate through every possible combination in array
        ## to find one that adds up to target value
        lenNums = len(nums)
        for i in range(lenNums):
            for j in range(i + 1, lenNums):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return [0,0]