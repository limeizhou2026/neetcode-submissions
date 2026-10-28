class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #1. dp[j]:背包为j装满之后的最大重量/价值
        #2. 推导公式
        #3. initialization：dp[0] = 0 非零下标也为0
        #4. 遍历顺序：先物品后背包 并从大往小遍历 这样才会每个物品只被取一次
        #5. 打印数组

        total_stone = sum(stones)
        target = total_stone//2
        dp = [0] *(target+1)

        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j-stone]+stone)

        return total_stone - dp[target] - dp[target]