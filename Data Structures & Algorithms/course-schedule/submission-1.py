class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = [0] * numCourses
        taken = set()
        q = deque()
        adj = [[] for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            count[course] += 1
            adj[prerequisite].append(course)

        for course in range(numCourses):
            if count[course] == 0:
                q.append(course)
        
        while q:
            current = q.popleft()
            taken.add(current)
            for course in adj[current]:
                    count[course] -= 1
                    if count[course] == 0:
                        q.append(course)
        
        n = len(taken)

        return numCourses == n
