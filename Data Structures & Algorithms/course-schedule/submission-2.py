class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numPrereqs = [0] * numCourses # numPrereqs[i] = numPrereqs for course i
        adjList = [[] for i in range(numCourses)]

        # Fill the adjList and numPrereqs for every course-prereq pair
        # Prereq is source, which points to course (destination)
        for course, prereq in prerequisites:
            numPrereqs[course] += 1
            adjList[prereq].append(course)

        q = deque()

        # Add course with 0 prereqs to the q (start of topological order)
        for courseNum in range(numCourses):
            if numPrereqs[courseNum] == 0:
                q.append(courseNum)
        
        # Number of "finished" nodes (no cycle if finish == numCourses)
        # A course is finished if we have successfully taken it
        finish = 0
        while q:
            node = q.popleft()
            # Mark it as finished
            finish += 1
            for neighbor in adjList[node]:
                # Mark it as finished
                numPrereqs[neighbor] -= 1
                if numPrereqs[neighbor] == 0:
                    q.append(neighbor)
        return finish == numCourses