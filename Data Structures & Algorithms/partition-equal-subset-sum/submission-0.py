class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #1. dp【j】：容量为j的背包 所能背的最大价值是dp【j】
        #这道题的重量和value都可以是nums【i】
        #2. 推导公式：dp[j]=max(dp[j], dp[j-nums[i]]+nums[i])
        #3. initalization：dp[0] = 0
        #4. 遍历顺序：从物品到背包 倒序
        #5. 打印dp数组
        n = len(nums)

        total_num = sum(nums)
        #if a set can be divided into 2 equal sum sets, then the total should be even
        if total_num % 2 ==1:
            return False
        target = total_num // 2
        dp = [0] * (target+1)
        dp[0] =0
        #先scan 物品
        for num in nums:
            #再scan背包
            for j in range(target, num-1, -1):
                #这道题的weight 和 value 都是nums【i】
                dp[j] = max(dp[j], dp[j-num]+num)

        #如果这个背包的容量 刚好等于它的价值 说明能找到一样的和
        if dp[target] == target:
            return True

        return False
