class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an empty list to represent the directed graph
        adj = [[] for _ in range(numCourses)]
        # Create an empty list to store the number of incoming edges
        indegree = [0] * numCourses
        # Create a list to store the topological order of the courses
        ans = []

        # Build the graph by iterating over the prerequisites
        for pair in prerequisites:
            course, prereq = pair[0], pair[1]
            adj[prereq].append(course)
            indegree[course] += 1
        
        # Perform the topological sort using Kahn's algorithm
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            ans.append(curr)

            for next_course in adj[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return len(ans) == numCourses
