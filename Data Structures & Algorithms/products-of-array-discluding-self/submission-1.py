class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalSum = 1;
        hasZero = False
        for num in nums:
            if num == 0 and hasZero != True:
                hasZero = True
                continue;
            totalSum *= num
            

        results = []
        for num in nums:
            if hasZero and num != 0:
                results.append(0)
            elif hasZero and num == 0:
                results.append(totalSum)
            else:
                results.append(int(totalSum / num))
        return results