class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window + hash map
        # two ptrs l, r
        # Make hash map for target str s1
        # For each window, calculate hash map of substring and if they are the same, return true
        # Else, return false

        count = {}
        l, ret = 0, 0

        s1_cnt = Counter(s1)

        print(s1_cnt)

        for r in range(len(s2)):
            if (r - l + 1) < len(s1):
                continue
            print(s2[l:r + 1])
            if Counter(s2[l:r + 1]) == s1_cnt:
                return True
            l += 1
        
        return False
            


        