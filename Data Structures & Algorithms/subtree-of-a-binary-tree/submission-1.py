# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True # Empty tree is a isSubtree
        if not root:
            return False
        
        # Do DFS, checking every node
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False
        elif root1.val != root2.val:
            return False
        else:
            # Values match in both trees, check children
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)