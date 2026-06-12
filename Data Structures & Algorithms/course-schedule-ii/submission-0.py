class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set() # Current DFS path (to detect cycles)
        visited = set() # Fully processed course
        res = []

        # Make map of course -> list(prerequisites)
        prereqMap = {course:[] for course in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        # Use dfs to find a cycle
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            
            cycle.add(node)
            for prereq in prereqMap[node]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(node)
            visited.add(node)
            # Add to result only after all of its prereqs have been processed
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
