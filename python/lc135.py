class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = [1] * n

        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                candy[i + 1] = candy[i] + 1

        for i in reversed(range(1, n)):
            candy[i] = max(candy[i], 1)
            if ratings[i] > ratings[i - 1]:
                candy[i] = max(candy[i - 1] + 1, candy[i])
            if ratings[i] < ratings[i - 1]:
                candy[i - 1] = max(candy[i - 1], candy[i] + 1)

        return candy


ratings1 = [1, 0, 2]
ratings2 = [1, 2, 87, 87, 87, 2, 1]
ratings3 = [1, 6, 3, 2, 5, 2, 1, 7, 6, 3]
ratings4 = [1, 3, 4, 5, 2]
s = Solution()
print(s.candy(ratings1))
print(s.candy(ratings2))
print(s.candy(ratings3))
print(s.candy(ratings4))
