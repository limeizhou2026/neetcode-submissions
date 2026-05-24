class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        y = 0
 
 
        for i in nums:
            if i == 1:
                x +=1
                y = max (x, y)
            elif i != 1:
                x = 0
        return y           