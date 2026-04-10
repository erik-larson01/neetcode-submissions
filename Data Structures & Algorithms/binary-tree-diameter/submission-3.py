# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            if not root:
                return 0
            nonlocal res
            # Get height of subtrees
            left = dfs(root.left)
            right = dfs(root.right)
            # Diameter is the sum of height of subtrees
            diameter = left + right
            res = max(res, diameter)
            return 1 + max(left, right)
        dfs(root)
        return res