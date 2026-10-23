class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
            
            