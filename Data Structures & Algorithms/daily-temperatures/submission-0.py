class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create monotonic stack - decreasing
        # When new element is added, pop all of the elemnts that are smaller than it

        stack = []
        ret = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temp, idx))
                continue
            while stack and stack[-1][0] < temp:
                _, old_idx = stack.pop()
                ret[old_idx] = idx - old_idx
            stack.append((temp, idx))

        return ret
            