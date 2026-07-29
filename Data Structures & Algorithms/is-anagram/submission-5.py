class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsS = dict()
        charsT = dict()

        for charS in s:
            if charS not in charsS:
                charsS[charS] = 1
            else:
                charsS[charS] += 1

        for charT in t:
            if charT not in charsT:
                charsT[charT] = 1
            else:
                charsT[charT] += 1
        
        if charsS == charsT:
            return True
        return False

