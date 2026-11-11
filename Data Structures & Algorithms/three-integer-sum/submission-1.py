class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #先把nums sort一下 这样有两个好处：1. 下一个num如果还是一样的数就可以跳过 因为找到的elements还是一样的 2.比如一个正数需要找负数 但如果在最小正数位置之前都没有找到 那后面就不用找啦
        #再用一个l， r pointer 从左右开始找 大了r往左 小了l往右
        #找到为这个数相反的和的elements 之后继续找 

        res = []

        nums.sort()
        n = len(nums)

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue
            if value>0:
                break

            l = i+1
            r = n-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    #KEY：如果要用一个triplets list 那每次就都要reset成空【】 不然list会一直append每一轮的elements
                    res.append([nums[i], nums[l], nums[r]])
                    #KEY：在找到一个正确的组合之后 应该继续挪动位置 找是否有下一轮正确答案
                    l+=1
                    r-=1
                    #KEY：由于上面刚刚把l和r的位置变动了
                    #KEY：应该找到刚才的位置是 r+1 和现在的r比 是不是重复
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                    #KEY：找到刚才的位置应该是 l-1 和现在的l比 是否重复
                    while l<r and nums[l] == nums[l-1]:
                        l+= 1
                elif total < 0:
                    l+=1
                else:
                    r-=1


        return res






































        triplets = []
        res = []
        if not nums:
            return []

        n =len(nums)
        #nums.sort()会返回None 所以不能用variable去接
        nums.sort()

        #enumerate 找到index和val
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
                #如果val》0 后面的数都比它大 不可能加起来为0
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
                    #因为要避免duplicate 如果下一个数和刚才这个数相同的话就没有必要再scan一遍
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1

        return res