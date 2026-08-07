# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ret = root
        queue = deque()
        if root:
            queue.append(root)
        while len(queue) > 0:
            root = queue.popleft()
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp

        return ret