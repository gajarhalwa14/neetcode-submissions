# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        ret = []
        queue.append((root, 0))
        while len(queue) > 0:
            curr_tuple = queue.popleft()
            curr, depth = curr_tuple[0], curr_tuple[1]
            if curr.left:
                queue.append((curr.left, depth + 1))
            if curr.right:
                queue.append((curr.right, depth + 1))
            if len(ret) <= depth:
                ret.append([])
            ret[depth].append(curr.val)

        return ret
