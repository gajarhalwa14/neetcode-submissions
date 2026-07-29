class Solution:
    def trap(self, height: List[int]) -> int:
        # take 2 pointer l, r
        # If 
        # While height[l] > height[r], move r to the right and add difference of height[l] and height[r]
        # If height[l] <= height[r], add amount added to total, set l equal to r and r += 1, continue
        # Edge cases: if r keeps decreasing adn doesnt ever increase, no water can be put there, so discard

        l, r = 0, 0
        ret = 0
        capacity = 0
        last_r = height[r]
        while r < len(height):
            if l == r:
                last_r = height[r]
                r += 1
                continue
            if height[l] > height[r]:
                if height[r] > last_r:
                    to_add = 0
                    if height[r - 2] < height[r]:
                        to_add = height[r] - max(height[r-2], last_r) + height[r] - last_r
                    else:
                        to_add = height[r] - last_r
                    ret += to_add
                    capacity -= to_add
                capacity += height[l] - height[r]
                last_r = height[r]
                r += 1
            else:
                ret += capacity
                capacity = 0
                l = r

        return ret
        