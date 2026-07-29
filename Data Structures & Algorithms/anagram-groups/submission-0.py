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
        


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lenStrs = len(strs)
        if lenStrs == 1:
            return [[strs[0]]]
        wordIdx = [-1] * lenStrs
        counter = 0
        for i in range(lenStrs):
            for j in range(i + 1, lenStrs):
                if self.isAnagram(strs[i], strs[j]):
                    if wordIdx[i] != -1:
                        wordIdx[j] = wordIdx[i]
                    elif wordIdx[j] != -1:
                        wordIdx[i] = wordIdx[j]
                    else:
                        wordIdx[i] = counter
                        wordIdx[j] = counter
                        counter += 1

        retList = []
        for i in range(lenStrs):
            if wordIdx[i] == -1:
                retList.append([strs[i]])

        checkCounter = 0
        while checkCounter < counter:
            anagrams = []
            for idx in range(lenStrs):
                if wordIdx[idx] == checkCounter:
                    anagrams.append(strs[idx])
            retList.append(anagrams)
            checkCounter += 1
        
        return retList