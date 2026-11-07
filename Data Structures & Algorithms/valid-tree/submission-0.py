class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        from collections import deque
        q = deque()
        visited = set()

        if not edges or n == 0:
            return True

        if len(edges) != n-1:
            return False

        for node1, node2 in edges:
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []

            graph[node1].append(node2)
            graph[node2].append(node1)

        for node in graph:
            q.append(node)
            visited.add(node)
            break

        while q:
            current = q.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)

        return len(visited) == n