class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
        

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x ==y:
                continue
            elif x < y:
                heapq.heappush(heap, -(y-x))

        if len(heap) < 1:
            return 0
        else:
            result = -heapq.heappop(heap)
    
        return result
