class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp1 = 2
        dp2 = 1

        for i in range(3, n+1):
            dpi = dp1 + dp2
            dp2 = dp1
            dp1 = dpi

        return dp1 













































        if n <= 2:
            return n

        dp = [n] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp
        