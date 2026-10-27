class Solution:
    def integerBreak(self, n: int) -> int:
        #dp[i]的含义：int i拆成k个int相乘的最大prodcut
        #推导公式
        #initialization：dp【2】 =1
        #遍历顺序：https://meet.google.com/meet/qng-sttd-ach?authuser=0
        #打印数组

        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*dp[i-j], j*(i-j))

        return dp[n]