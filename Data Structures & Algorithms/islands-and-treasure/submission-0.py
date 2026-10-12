class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        m= len(grid)
        n=len(grid[0])
        INF = 2147483647
        directions = [(-1, 0), (0, -1), (1, 0), (0,1)]
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    continue
                q.append([r, c, 0])

        while q:
            r, c, steps = q.popleft()
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if nr < 0 or nr>= m or nc <0 or nc>= n or grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = steps+1
                q.append([nr, nc, steps +1])
        
        

