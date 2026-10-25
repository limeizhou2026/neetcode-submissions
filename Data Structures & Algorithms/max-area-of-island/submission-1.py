class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        max_area = 0

        def dfs(r,c):
            nonlocal area
            if r<0 or r>=rows or c <0 or c>= cols:
                return 0
            
            if grid[r][c] == 0:
                return 0
            #key: 要把访问过的cell变成0 这这样才不会造成多次访问
            grid[r][c] = 0
            area += 1

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                #因为 dfs 里的 nonlocal area 让它使用外层函数的同一个 area，而不是创建自己的局部变量，所以dfs 不用return， 外层for loop里面的area也知道了变化后的数值

                area = 0
                dfs(i, j) 
                max_area = max(max_area, area)
        return max_area
                


































        rows = len(grid)
        cols = len(grid[0])
        area = 0
        max_area = 0

        def dfs(r, c):
            nonlocal area
            if r>=rows or r<0 or c>=cols or c<0:
                return
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            area += 1
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                area = 0
                dfs(i, j)
                max_area =max(max_area, area)

        return max_area



                