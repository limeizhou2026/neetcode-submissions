class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #using set to remove duplicates
        #set a length to count the length of the consecutive sequence
        #if num-1 not in nums which means this is a new sequence needed to count; reset length as 0
        #otherwise continously incremente num until num+1 no longer in nums; update the maxval afterwards

        length = 0
        maxval = 0
        numset = set(nums)

        for num in nums:
            if num-1 not in numset:
                length = 1
                while num+1 in numset:
                    length+=1
                    num+=1
                    

              
                maxval = max(maxval, length)

        return maxval



































            
            