class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #1.确定dp【i】的意义：每一步台阶要往上爬应付的cost
        #2.确定dp推导公式dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]cost[i-2])
        #3.initialization: dp[0]=0, dp[1]=0
        #4.确定遍历顺序：bottom-up；左右
        #5.举例打印数组
        n = len(cost)
        dp=[0]* (n+1)
        if n<=1:
            return
        dp[1] = 0
        dp[0] = 0

        for i in range(2, n+1):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[n]




























        #using DP
        #最重要的点是理解在stair 1 或0 是不花钱的！！！只有往上走才要花钱
        #1. 确定dp数组以及下标的含义：到达阶梯i需要的最少cost是dp
        #2. 确定递推公式：dp[i] =min((dp[i-1]+cost[i-1]), (dp[i-2]+cost[i-2]))
        #3. dp数组初始化：dp[0] = 0, dp[1] =0
        #4. 确定遍历顺序：从前向后，后面是由前面决定的
        #5. 打印数组
        n=len(cost)

        if n<= 1:
            return 0
        dp = [0]*(n+1)
        dp_2 = 0
        dp_1 = 0
        for i in range(2, n+1):
            dp_c = min(dp_1+cost[i-1], dp_2+cost[i-2])
            dp_2 = dp_1
            dp_1 = dp_c
        return dp_1