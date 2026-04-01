# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Check if both left and right subtrees are balanced
            subtreeBalance = left[0] and right[0]

            # A node is balanced iff subtreeBalance and height differs by <= 1
            isBalanced = subtreeBalance and abs(left[1] - right[1]) <= 1

            # Return list of [isBalanced, nodeHeight
            return [isBalanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]