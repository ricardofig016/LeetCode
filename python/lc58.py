class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        while not s[i].isalpha():
            i -= 1
        while s[i] != " " and i >= 0:
            length += 1
            i -= 1
        return length


str = "   fly me   to   the moon  "
s = Solution()
print(s.lengthOfLastWord(str))
