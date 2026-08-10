# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Tuple  = (node, minVal, maxVal)
        queue = deque()
        queue.append((root, float('-inf'), float('inf')))

        while queue:
            curr_tuple = queue.popleft()
            curr, minVal, maxVal = curr_tuple[0],curr_tuple[1], curr_tuple[2]
            if curr.left:
                if curr.left.val >= curr.val or curr.left.val <= minVal:
                    return False
                else:
                    queue.append((curr.left, minVal, curr.val))
            if curr.right:
                if curr.right.val <= curr.val or curr.right.val >= maxVal:
                    return False
                else:
                    queue.append((curr.right, curr.val, maxVal))
        return True
            