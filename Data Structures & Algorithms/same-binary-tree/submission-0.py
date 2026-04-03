# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(rootP, rootQ):
            # Check if both are null
            if not rootP and not rootQ:
                return True
            if rootP and rootQ and rootP.val == rootQ.val:
                # Both values match
                return dfs(rootP.left, rootQ.left) and dfs(rootP.right, rootQ.right)
            else:
                return False
        return dfs(p,q)
