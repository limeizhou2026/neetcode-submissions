class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp【j】到第i号房 包括i的所有房间 能偷到的最大值 就是dp[i]=dp[nums.size()-1]也就是dp【ums的最后一个值】
        #2. 推导公式：
        #偷i：dp[i-2]+nums[i]  因为如果不偷i 那到第前2个可以偷
        #不偷i: dp[i-1]  i不偷的话  i前面一个就可以偷
        #3. initialization：
        #4. 遍历顺序： i从小到大 
        #5. 打印数组检查 数组是否有问题
        

        n = len(nums)
        dp = [0] * (n)

        #edge case
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp[0] = nums[0]
        #dp[1] 应该是0和1 之间的最大值 因为相邻的不能偷 所以只能偷更大的一家
        dp[1] = max(nums[0], nums[1])

        #遍历顺序应该从2开始 因为0和1都已经scan过了
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        #最后一个num的位置就是dp【i】
        return dp[n-1]