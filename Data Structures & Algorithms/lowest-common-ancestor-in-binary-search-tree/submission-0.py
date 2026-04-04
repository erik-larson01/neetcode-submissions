# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        
        # Check if both descendants are in the left subtree
        if max(p.val, q.val) < root.val:
            # Traverse left
            return self.lowestCommonAncestor(root.left, p, q)
        # Check if both descendants are in the right subtree
        elif min(p.val, q.val) > root.val:
            # Traverse right
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # The current node is the ancestor as the descendants are split
            return root