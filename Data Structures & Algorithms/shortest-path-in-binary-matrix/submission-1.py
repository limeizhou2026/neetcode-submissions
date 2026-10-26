class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q=deque()

        if grid[0][0] or grid[n-1][n-1]:
            return -1

        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(1,-1),(-1,1)]
        q.append([0,0,1])

        while q:
            r,c,length = q.popleft()
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                if nr < 0 or nr>=n or nc<0 or nc>=n:
                    continue
                
                if grid[nr][nc] == 1:
                    continue
                grid[nr][nc] = 1
                q.append([nr,nc,length+1])
            if r == n-1 and c == n-1:
                    return length
        return -1






































        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        #
        q = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))
        direction = [(0,1), (1, 0), (-1,0), (0,-1), (1, 1), (-1, -1), (-1,1), (1, -1)]

        while q:
            r, c, length = q.popleft()
            if r == n-1 and c == n-1:
                return length
            
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if  0<= nr <n and (0<= nc <n) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    #make sure to add double brackets as a tuple inside
                    q.append((nr, nc, length+1))
                    #same as above
                    visited.add((nr, nc))
        
        return -1
