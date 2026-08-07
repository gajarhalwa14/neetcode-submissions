# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            return 1 + max(left, right)

        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not left or not right:
            return False

        if abs(dfs(root.left) - dfs(root.right)) > 1:
            return False

        return True
        

