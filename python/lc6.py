class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        rows = [[] for i in range(numRows)]
        i = 0
        slope = +1
        for ch in s:
            rows[i].append(ch)
            if i == 0:
                slope = +1
            elif i == numRows - 1:
                slope = -1
            i += slope
        words = ["".join(i) for i in rows]
        return "".join(words)


string = "PAYPALISHIRING"
numRows = 3
s = Solution()
print(s.convert(string, numRows))
