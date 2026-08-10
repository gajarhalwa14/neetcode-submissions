# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        queue = deque()
        queue.append((root, root.val))
        while len(queue) > 0:
            isGood = False
            curr_tuple = queue.popleft()
            curr, maxVal = curr_tuple[0], curr_tuple[1]
            if curr.val >= maxVal:
                isGood = True
                ret += 1
            if curr.left:
                if isGood:
                    queue.append((curr.left, curr.val))
                else:
                    queue.append((curr.left, maxVal))
            if curr.right:
                if isGood:
                    queue.append((curr.right, curr.val))
                else:
                    queue.append((curr.right, maxVal))
            
        return ret
            


        