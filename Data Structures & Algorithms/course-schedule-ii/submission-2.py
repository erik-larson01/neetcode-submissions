class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        numPrereqs = [0] * numCourses
        adjList = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            numPrereqs[course] += 1
            adjList[prereq].append(course)
        
        q = deque()
        for courseNum in range(numCourses):
            if numPrereqs[courseNum] == 0:
                q.append(courseNum)
        
        finish = 0
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            finish += 1
            for neighbor in adjList[node]:
                numPrereqs[neighbor] -= 1
                if numPrereqs[neighbor] == 0:
                    q.append(neighbor)
        return res if finish == numCourses else []