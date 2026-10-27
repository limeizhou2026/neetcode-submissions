class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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



         
              