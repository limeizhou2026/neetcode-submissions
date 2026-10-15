class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap using the unique num as key, then count the frequency of each. return the num whose frequency is equal or bigger than k
        hashmap_n = {}
        result = []
        for num in nums:
            key = num
            if key in hashmap_n:
                hashmap_n[key] = hashmap_n.get(key, 0) + 1
                
            else:
                hashmap_n[key] = 1

        sorted_items = sorted(hashmap_n.items(), key = lambda item: item[1], reverse=True)

        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result