class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        idx = -1
        first, second = (0, 0)
        while first < len(haystack):
            while second - first < len(needle) and second < len(haystack):
                if needle[second - first] == haystack[second]:
                    second += 1
                else:
                    break
            if second - first == len(needle):
                print("first:", first)
                print("second:", second)
                return first
            first += 1
            second = first
        return idx


haystack = "leetcode"
needle = "leeto"
s = Solution()
print(s.strStr(haystack, needle))
