# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # Use BFS
        queue = deque()
        queue.append(root)
        while queue:
            queueLength = len(queue)
            level = []
            # For all nodes in the queue, add neighbors if they exist to queue
            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            # If all children are null, level could be [] (False)
            if level:
                res.append(level)
        return res