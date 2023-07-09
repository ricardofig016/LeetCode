class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = [0] * n
        max_total = 0
        for i in range(n - 2, -1, -1):
            max_i = 0
            j = i + 1
            while j < n:
                if j > i:
                    max_i = max(max_i, prices[j] - prices[i] + profit[j])
                    break
                else:
                    j += 1

            profit[i] = max_i
            max_total = max(max_total, max_i)

        return max_total


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
max = s.maxProfit(prices)
print(max)
