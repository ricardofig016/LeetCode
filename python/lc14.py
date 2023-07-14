class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        i = 0
        prefix = strs[i]
        while prefix != "" and i < n - 1:
            j = 0
            while j < len(prefix) and j < len(strs[i + 1]):
                if prefix[j] != strs[i + 1][j]:
                    prefix = prefix[:j]
                j += 1
            if len(strs[i + 1]) < len(prefix):
                prefix = strs[i + 1]
            i += 1

        return prefix


strs = ["flower", "flow", "flight"]
s = Solution()
print(s.longestCommonPrefix(strs))
