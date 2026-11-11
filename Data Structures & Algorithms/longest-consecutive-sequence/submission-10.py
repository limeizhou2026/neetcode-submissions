class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #先把nums变成set消除duplicates
        #再用for loop在一个个去尝试 是第一个的话count = 1 不是的话就count+=1

        maxcount = 0

        count = 0
        numSet = set(nums)

        for num in numSet:
            if (num-1) not in numSet:
                count = 1
                current = num
                while current+1 in numSet:
                    current+=1
                    count+=1
            maxcount = max(maxcount,count)
        return maxcount



































        nums = set(nums)
        count = 0
        maxlen= 0
        for num in nums:
            if num-1 not in nums:
                count = 1
                while num+count in nums:
                    count+=1
                maxlen = max(maxlen, count)

        return maxlen
































        length = 0
        max_len = 0
        numSet = set(nums)

        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num+length) in numSet:
                    length+=1
                max_len=max(max_len, length)

        return max_len
            
            