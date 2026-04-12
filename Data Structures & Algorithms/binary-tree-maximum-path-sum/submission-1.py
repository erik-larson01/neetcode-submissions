# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            # Get sum of subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # Ensure subtrees are nonnegative
            leftMax = max(left, 0) 
            rightMax = max(right, 0)

            # Calculate the best path through the node (up and over)
            pathThroughNode = node.val + leftMax + rightMax
            res = max(res, pathThroughNode)

            # Return path including the node
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res