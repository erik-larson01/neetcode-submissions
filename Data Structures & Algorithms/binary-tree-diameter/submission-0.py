# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use list as mutable int (or nonlocal)
        res = [0]

        # Do DFS 
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            # Update max diameter
            res[0] = max(res[0], left + right)

            # Height returned to parent
            return 1 + max(left, right)
        dfs(root)
        return res[0]