class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #完全背包
        #dp[i]:装满容量j的最少物品是多少;凑出金额i 最少需要几枚硬币
        #dp[0] = 0
        dp = [1e9] * (amount+1)
        dp[0] = 0

        if len(coins) == 0:
            return 0

        for i in range(len(coins)):
            #key：从当前硬币的面值开始， 一直尝试凑到目标金额；因为coin i 一旦选中了就不可能凑成比他小的数 所以要从 coin i开始考虑目标amount
            for j in range(coins[i], amount+1):
                if dp[j-coins[i]] != 1e9:
                    dp[j] = min(dp[j-coins[i]]+1, dp[j])
        
        if dp[amount] == 1e9:
            return -1
        return dp[amount]


        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0

            if amount <0:
                return -1
            
            if amount in memo:
                return memo[amount]
            res = float("inf")
            for coin in coins:
                if amount-coin >= 0:
                    res = min(res, dfs(amount-coin)+1)
            memo[amount] = res

            return res

        mincoin = dfs(amount)
        if mincoin >= float("inf"):
                return -1
        else:
                return mincoin



         
              