# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfsIsValid(node, leftBound, rightBound):
            # Base Case
            if not node:
                return True
            if not (leftBound < node.val < rightBound):
                return False
            
            # Check left and right subtrees
            left = dfsIsValid(node.left, leftBound, node.val)
            right = dfsIsValid(node.right, node.val, rightBound)

            # If both left and right subtrees are valid, the node is valid
            return left and right
        return dfsIsValid(root, float("-inf"), float("inf"))