class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1.用一个hashmap储存每个num出现的频率作为value； num作为key
        #2.按照value排序hashmap 然后把所有的key按顺序append到list里面 in desending order
        #3.print从0到index k的num

        hashnums = {}
        res = []

        for num in nums:
            hashnums[num] = hashnums.get(num, 0) +1

        sorted_hash = sorted(hashnums.items(), key=lambda item:item[1], reverse = True)

        n  = len(sorted_hash)
        for i in range(n):
            res.append(sorted_hash[i][0])

        return res[:k]

































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