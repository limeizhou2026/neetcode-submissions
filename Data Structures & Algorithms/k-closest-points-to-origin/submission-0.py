class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            distance = ((points[i][0] - 0)**2 + (points[i][1] - 0)**2)
            heapq.heappush(heap, (distance, i))

            result= []
        for j in range(k):

            distance, index = heapq.heappop(heap)
            result.append(points[index])

        return result
