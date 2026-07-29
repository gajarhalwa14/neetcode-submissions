class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # totalSum = 1;
        # hasZero = False
        # for num in nums:
        #     if num == 0 and hasZero != True:
        #         hasZero = True
        #         continue;
        #     totalSum *= num
            

        # results = []
        # for num in nums:
        #     if hasZero and num != 0:
        #         results.append(0)
        #     elif hasZero and num == 0:
        #         results.append(totalSum)
        #     else:
        #         results.append(int(totalSum / num))
        # return results

        ############# WITHOUT DIVISION ###################
        output = [0] * len(nums)

        # Prefix computation
        for i in range(len(nums)):
            if i == 0:
                output[i] = 1
                continue
            output[i] = output[i - 1] * nums[i - 1]

        # Postfix computation
        postfix = 1;
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            postfix *= nums[i + 1]
            output[i] *= postfix
        
        return output
