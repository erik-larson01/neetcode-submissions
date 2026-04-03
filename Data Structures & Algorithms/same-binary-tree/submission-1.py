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
            elif rootP and not rootQ or rootQ and not rootP:
                # One is null one has a value
                return False
            elif rootP.val != rootQ.val:
                # Both are not null with differing values
                return False
            else:
                # Nodes are equal value and not null
                return dfs(rootP.left, rootQ.left) and dfs(rootP.right, rootQ.right)
        return dfs(p,q)
