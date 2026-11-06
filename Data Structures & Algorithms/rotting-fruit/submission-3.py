class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #create一个helper function -bfs 去traverse每个adj cell，如果有1 就变成2 如果是0就return 每变一次min+1
        #然后设定从2开始traverse
        minutes = 0
        from collections import deque
        q = deque()
        visited_rotten = set()
        fresh = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        if not len(grid) or not len(grid[0]):
            return 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited_rotten.add((i,j))

        while q and fresh > 0:         
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = dr+r
                    nc = dc +c
                
                    if nr < 0 or nr>=rows or nc<0 or nc>= cols:
                        continue

                    if grid[nr][nc] == 0 or (nr,nc) in visited_rotten:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1

                        q.append((nr,nc))
                        visited_rotten.add((nr,nc))
            minutes += 1
                
        if fresh == 0:
            return minutes
        else:
            return -1













































        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0
        rotten = set()
        direction = [(-1,0), (1,0), (0,-1), (0,1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                    rotten.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
      
        while q:
                r, c, time = q.popleft()
                minutes = time

                for dr, dc in direction:
                    nr, nc = r+dr, c+dc

                    if 0<= nr <rows and 0<= nc <cols and grid[nr][nc] == 1 and (nr, nc) not in rotten:
                        q.append((nr, nc, time+1))
                        rotten.add((nr, nc))
                        fresh -= 1
        if fresh == 0:
            return minutes
        else:
            return -1
