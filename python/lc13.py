class Solution(object):
    def romanToIntHelper(self, char):
        if char == "I":
            return 1
        if char == "V":
            return 5
        if char == "X":
            return 10
        if char == "L":
            return 50
        if char == "C":
            return 100
        if char == "D":
            return 500
        if char == "M":
            return 1000

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        literal = [self.romanToIntHelper(s[i]) for i in range(n)]
        number = 0
        max_lit = literal[0]
        for i in range(n):
            if literal[i] > max_lit:
                number -= max_lit
                max_lit = literal[i] - literal[i - 1]
                number += max_lit
            else:
                number += literal[i]
                max_lit = literal[i]
        return number


roman = "MCMXCIV"  # 1994
s = Solution()
print(s.romanToInt(roman))
