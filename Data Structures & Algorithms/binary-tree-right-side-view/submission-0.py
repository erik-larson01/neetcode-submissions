# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # The right side view is the last node per level
        res = []
        q = deque()
        q.append(root)

        # Use BFS
        while q:
            # Get nodes in level
            nodesInLevel = len(q)
            level = []
            for i in range(nodesInLevel):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # Add children to queue
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level[-1])
        return res