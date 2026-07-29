class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        Lp = 0
        Rp = n-1

        while Lp <= Rp:
            mid = (Lp + Rp) // 2

            
            if target > nums[mid]:
                Lp = mid+1

            elif target < nums[mid]:
                Rp = mid-1

            elif target == nums[mid]:
                return mid
            
        
        return -1

            



