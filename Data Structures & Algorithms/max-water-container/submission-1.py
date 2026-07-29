class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force way: use two pointers, calculate every single container size and keep the max
        # [2, 7, 12, 3, 18, 10, 4, 7, 11]
        # [1, 5, 10, 15, 20, 25, 34, 35]
        # max = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         capacity = min(heights[i], heights[j]) * (j - i)
        #         if capacity > max:
        #             max = capacity
        
        # return max

        # This is inefficient bc we are calculating capacity every time.
        # We dont need to do this bc we know that as j increases, if heights[j] > heights[i]
        # then the capacity will increase, meaning we don't have the calculate the capacities in between

        # Use sliding window: take ith element and last element. If i <= last element, calculate capacity
        # and compare w/ max. If i > last element, slide window until it is

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            capacity = (r - l) * min(heights[l], heights[r])
            res = max(res, capacity)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
            
            
