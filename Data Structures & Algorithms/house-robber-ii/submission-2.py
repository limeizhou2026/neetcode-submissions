class Solution:
    def rob(self, nums: List[int]) -> int:
        #1. dp【j】到第i号房 包括i的所有房间 能偷到的最大值 就是dp[i]=dp[nums.size()-1]也就是dp【ums的最后一个值】
        #2. 推导公式：
        #偷i：dp[i-2]+nums[i]  因为如果不偷i 那到第前2个可以偷
        #不偷i: dp[i-1]  i不偷的话  i前面一个就可以偷
        #3. initialization：
        #4. 遍历顺序： i从小到大 
        #5. 打印数组检查 数组是否有问题

        #这道题不同于House Robber i，这是道环形题，也就是头尾链接 不能都选。因此我们可分为三种senario：
        #1. 假设有5个房间，我们只考虑中间三间。不要头尾
        #2. 把头部也加进来考虑 至于选不选头部 推导公式会找到答案
        #3. 把尾部考虑进来 不要头部 选不选尾部 推导公式会找到答案
        #其实第二 第三种情况都包含了第一种 所以我们考虑后两者就好
        #因此这道题只需要把house robber i的逻辑放到一个helper function里面  把前两者的范围作为argument传进去就好
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        res1 = self.helper(nums[:len(nums)-1])
        res2 = self.helper(nums[1:len(nums)])

        return max(res1, res2)

    def helper(self, nums: List[int]) -> int:

        #calculate the length of the array
        n = len(nums)
        #initialize the dp list
        dp = [0]*n
        #edge case
        if n == 1:
            return nums[0]
        #initialization
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[n-1]

























        #due to the constraints: the length is no less than 1, we dont have to consider when the nums is not true
        if len(nums) == 1:
            return nums[0]

        res1 = self.helper(nums[1:])
        #这里由于还没开始计算nums的长度， 所以不能用n-1, 可用-1表示最后一个num或者用len（nums）
        res2 = self.helper(nums[:-1])

        return max(res1, res2)

    def helper(self, nums: List[int]) -> int:
            n = len(nums)
            dp = [0] * n
            #因为传进来的nums是切片 所以要考虑是0的情况
            if len(nums) == 0:
                return 0

            if len(nums) == 1:
                return nums[0]

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i]=max(dp[i-1], dp[i-2]+nums[i])

            return dp[n-1]