class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key, value in hashmap.items():
            if value > 1:
                return key