class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #using DP
        #1. 确定dp[i][j]和下标的含义：走到grid【i】【j】的path一共是多少种
        #2. 确定推导公式：
        #3. initialization
        #4. 数组举例
        #5. 打印出数组

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            dp[i][0] =1
        for j in range(n):
            dp[0][j] =1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]