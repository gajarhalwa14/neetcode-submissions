import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        l, r, ret = 0, 1, 1
        length = 1
        letters = {}
        letters[s[l]] = l
        while r < len(s):
            if s[r] not in letters or letters[s[r]] < l:
                letters[s[r]] = r
                length += 1
                r += 1
            else:
                if length > ret:
                    ret = length
                l = letters[s[r]] + 1
                letters[s[r]] = r
                length = r - l + 1
                r += 1
        if length > ret:
            ret = length

        print(letters)
        print(length)
        print(l, r)
        return ret
        