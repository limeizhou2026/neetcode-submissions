class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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
