class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Dir edges from a to b for prerequisites[i] = [a, b]
        # For [a, b] b is a prereq of a

        visited = set()
        prereqMap = {}
        for i in range(numCourses):
            prereqMap[i] = []

        for course, prereq in prerequisites:
            prereqMap[prereq].append(course) # Prereq X-> Courses that depend on X
        
        # Use DFS to find a cycle in the graph
        def dfs(node):
            # If there is a cycle, it is not possible to finish all courses
            if node in visited:
                return False

            # If node has no prereqs left, it is safe.
            if prereqMap[node] == []:
                return True
            
            # Visit neighbors
            visited.add(node)
            for prereq in prereqMap[node]:
                if not dfs(prereq):
                    return False

            visited.remove(node) # Only keep track of current DFS path

            # This node and everything reachable from it contains no cycle
            # So we can remove its prereq list to hit a base case instead of checking neighbors again
            prereqMap[node] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True