class Solution:
    def climbStairs(self, n: int) -> int:
        #using DP 
        #1. dp[i] means how many ways to get to the stair i
        #2. 确定递推公式： dp[i] = dp[i-1] +dp[i-2]
        #3. Initalization: per constraints: n>0; so starting from 1; dp[i] = 1, dp[2] =2
        #4. 确定traverse order：bottom-up 因为后一个数是由前两个数决定的
        #5. 举例推导数组

        if n <= 2:
            return n
        
        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
































        #optimized bottom-up：only store the previous 2 dp amounts: Space O(1) Time O(n)
        if n <= 2:
            return n

        dp1 = 2
        dp2 = 1

        #using for loop to calculate the dp amount in the range of the known condition +1 to n+1 since Python does not include the upper bound in teh range
        for i in range(3, n+1):
            #current dp equals the sum of the previous 2 dp smounts
            dpi = dp1 + dp2
            #update the dp[i-2] with dp[i-1]
            dp2 = dp1
            #update the dp[i-1] with dp[i]
            dp1 = dpi

        #return dp1 since it stores teh current dp mount evetually
        return dp1 












































        #bottom-up: using a array to store all the dp amounts: Space O(n) Time O(n)
        if n <= 2:
            return n

        #initialize the array with 0 as the placeholder times n+1 since the number should be from 0 to n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            #continously compute the current dp amount
            dp[i] = dp[i-1] + dp[i-2]
        #return the amount of the index n of the dp array
        return dp[n]
        