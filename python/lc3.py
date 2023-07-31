class Solution(object):
    def lengthOfLongestSubstring(self, string):
        """
        :type s: str
        :rtype: int
        """
        n = len(string)
        if n <= 1:
            return n
        best_size = 0
        s, e = (0, 0)
        curr_substr = string[0]
        while s < n - 1 and e < n - 1:
            e += 1
            if string[e] in curr_substr:
                idx = curr_substr.index(string[e])
                curr_substr = curr_substr[idx + 1 :]
            curr_substr += string[e]
            best_size = max(best_size, len(curr_substr))
        return best_size


s = "_"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
