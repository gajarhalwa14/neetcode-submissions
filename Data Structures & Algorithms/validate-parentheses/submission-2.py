class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == ')':
                    if stack.pop() != '(': return False
                elif char == '}':
                    if stack.pop() != '{': return False
                else:
                    if stack.pop() != '[': return False
        if len(stack) > 0: return False
        return True

        