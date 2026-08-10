# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Modified DFS
        # Pop root, insert children - keep track if node from level has already been used in ret
        # Use tuple of (node, iepth)
        # Keep track of which levels are used with depth_dict
        # If key isnt in dict, add node to ret and set depth_dict[key] = True
        # We are able to get the right-facing nodes by appending the left child first and then right child

        if not root:
            return []
        ret = []
        stack = [(root, 0)]
        depth_dict = {}
        while len(stack) > 0:
            curr_tuple = stack.pop()
            curr, depth = curr_tuple[0], curr_tuple[1]
            if depth not in depth_dict:
                ret.append(curr.val)
                depth_dict[depth] = True
            if curr.left:
                stack.append((curr.left, depth + 1))
            if curr.right:
                stack.append((curr.right, depth + 1))

        return ret

        