class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        res = []
        if not nums:
            return []

        n =len(nums)
        #nums.sort()会返回None 所以不能用variable去接
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            if val > 0:
                break
            l = i+1
            r = n-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total>0:
                    r-= 1
                elif total < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1


        return res