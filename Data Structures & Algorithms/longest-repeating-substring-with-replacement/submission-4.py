class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window - 2 pointers l, r
        # While s[l] == s[r], r++ (and length)
        # If s[l] != s[r], decrement k and keep going until k cannot be decremented
        # When this happens, set l = r - k and keep going

        count = {}
        l, ret = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            ret = max(ret, r - l + 1)
        
        return ret
