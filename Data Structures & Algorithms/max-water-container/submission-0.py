class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force way: use two pointers, calculate every single container size and keep the max
        # [2, 7, 12, 3, 18, 10, 4, 7, 11]
        # [1, 5, 10, 15, 20, 25, 34, 35]
        max = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                num_water = min(heights[i], heights[j]) * (j - i)
                if num_water > max:
                    max = num_water
        
        return max