class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
            if value == 1:
                return key
