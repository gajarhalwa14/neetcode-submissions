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
        
        for ch in s:
            if ch not in charsT:
                return False
            if len(charsS) != len(charsT):
                return False
            if charsS[ch] != charsT[ch]:
                return False
        return True

