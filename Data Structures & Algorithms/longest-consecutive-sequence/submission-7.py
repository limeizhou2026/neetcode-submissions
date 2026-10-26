class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
            
            