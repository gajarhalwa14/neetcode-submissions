# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do inorder traversal, keep traversing until you get to the kth element in the list
        # Tuple: (node, hasExploredLeft)
        ret = 0
        numTraversed = 0
        stack = [[root, False]]
        while stack and numTraversed < k:
            curr_tuple = stack[-1]
            curr, hasExploredLeft = curr_tuple[0], curr_tuple[1]
            if not curr.left:
                stack[-1][1] = True
            if curr.left and not hasExploredLeft:
                stack[-1][1] = True
                stack.append([curr.left, False])
                continue
            ret = curr.val
            print(ret)
            numTraversed += 1
            
            stack.pop()
            if curr.right:
                stack.append([curr.right, False])
        
        return ret
            