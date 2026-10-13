class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        pacific = set()
        atlantic = set()
        result = []


        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr= dr +r
                nc = dc + c

                if nr<0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                if (nr, nc) in visited:
                    continue
                dfs(nr, nc, visited)
        #first row
        for c in range(cols):
            if (0, c) not in pacific:
                dfs(0, c, pacific)
        #first column
        for r in range(rows):
            if (r, 0) not in pacific:
                dfs(r, 0, pacific)
        #last row
        for c in range(cols):
            if (rows-1, c) not in atlantic:
                dfs(rows -1, c, atlantic)
        #last column
        for r in range(rows):
            if (r, cols-1) not in atlantic:
                dfs(r, cols-1, atlantic)

        for r, c in pacific:
            if (r,c) in atlantic:
                result.append([r,c])

        return result