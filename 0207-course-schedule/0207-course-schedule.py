class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from typing import List
        from collections import deque

        # Step 1: Create adjacency list
        graph = [[] for _ in range(numCourses)]

        # Step 2: Create indegree array
        indegree = [0] * numCourses

        # Step 3: Build graph
        for course, prerequisite_course in prerequisites:
            graph[prerequisite_course].append(course)
            indegree[course] += 1

        # Step 4: Add courses with indegree 0 to queue
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 5: Process courses
        completed_courses = 0

        while queue:
            current_course = queue.popleft()
            completed_courses += 1

            # Visit courses depending on current_course
            for next_course in graph[current_course]:
                indegree[next_course] -= 1

                # All prerequisites are completed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Step 6: If all courses are completed, no cycle exists
        return completed_courses == numCourses