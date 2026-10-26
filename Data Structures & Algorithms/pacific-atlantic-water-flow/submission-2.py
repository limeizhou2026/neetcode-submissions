class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
    #using BFS
    #set a pacific list to collect the cells that can flow into pacific；从pacific的两边出发。while create a corresponding list for Atlantic，从Atlantic的两边出发
    #the interacted cells are the result

        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        visitedp = set()
        visiteda = set()
        result = []
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
        for r in range(rows):
            for c in range(cols):
                
                if r == 0 or c == 0:
                    q.append([r, c])
                    pacific.add((r,c))
                    visitedp.add((r,c))

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                if nr <0 or nr>=rows or nc <0 or nc>=cols:
                    continue
                if heights[nr][nc] < heights[r][c] or (nr,nc) in visitedp:
                    continue
                visitedp.add((nr,nc))
                pacific.add((nr,nc))
                q.append([nr,nc])

        for r in range(rows):
            for c in range(cols):
                
                if r == rows-1 or c == cols-1:
                    q.append([r, c])
                    atlantic.add((r,c))
                    visiteda.add((r,c))

        while q:
            r,c = q.popleft()
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                if nr <0 or nr>=rows or nc <0 or nc>=cols:
                    continue
                if heights[nr][nc] < heights[r][c] or (nr,nc) in visiteda:
                    continue
                visiteda.add((nr,nc))
                atlantic.add((nr,nc))
                q.append([nr,nc])

        for i in pacific:
            if i in atlantic:
                result.append(list(i))

        return result







































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
                #next height should be bigger than current
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