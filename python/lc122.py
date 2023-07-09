class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size == 1:
            return 0

        left = 0
        right = 1
        max_p = 0
        while right < size:
            if prices[right] > prices[left]:
                max_p += prices[right] - prices[left]
            left += 1
            right += 1

        return max_p


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices))
