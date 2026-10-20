class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentp = 0
        maxp = 0
        n=len(prices)

        for i in range(n):
            for j in range(i+1, n):
                if prices[j] > prices[i]:
                    currentp = prices[j] - prices[i]
                    maxp = max(maxp, currentp)
                else:
                    continue

        return maxp