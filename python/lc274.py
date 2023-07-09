class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        n = len(citations)
        citations.sort(reverse=True)
        for i in range(n):
            if citations[i] >= i + 1:
                h = i + 1
        return h


citations = [3, 0, 6, 1, 5]
s = Solution()
print(s.hIndex(citations))
