class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqueChars = []
        for charS in s:
            if charS in uniqueChars:
                continue
            if (s.count(charS) != t.count(charS)):
                return False
            uniqueChars.append(charS)
        
        for charT in t:
            if charT not in uniqueChars:
                return False
        return True