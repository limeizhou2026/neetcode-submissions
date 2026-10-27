class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #1. 确定dp[i][j]的含义：走到cell【i】【j】的不同路径有多少种
        #2. 确认推导公式：
        #3. initialization：必须加一个条件确认第一行第一列没有障碍
        #4. 遍历顺序： 左右， 上下
        #5.打印数组
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]* n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                else:
                    continue

        return dp[m-1][n-1]