class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleanS = ""
        # for c in s:
        #     if c.isalnum():
        #         cleanS += c.lower()

        # reverse = ""
        # for i in range(len(cleanS) - 1, -1, -1):
        #     reverse += cleanS[i].lower()
        
        # if cleanS == reverse:
        #     return True
        # return False

        s = "".join(c for c in s if c.isalnum()).lower()

        if s == s[::-1]:
            return True
        return False
