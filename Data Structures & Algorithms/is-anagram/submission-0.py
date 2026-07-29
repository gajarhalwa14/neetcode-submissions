class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqueChars = []
        for charS in s:
            if charS in uniqueChars:
                continue
            if (s.count(charS) != t.count(charS)):
                return False
        
        for charT in t:
            if charT in uniqueChars:
                continue
            if (t.count(charT) != s.count(charT)):
                return False
        return True