class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


string = "the sky is blue"
s = Solution()
print(s.reverseWords(string))
