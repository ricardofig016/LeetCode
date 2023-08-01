class Solution(object):
    def findSubstring(self, string, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(string)
        m = len(words[0])
        s, e = (0, len(words[0]) * len(words))
        valid_idxs = []
        while e <= n:
            substrings = [string[i : i + m] for i in range(s, e, m)]
            if sorted(substrings) == sorted(words):
                valid_idxs.append(s)
            s += 1
            e += 1

        return valid_idxs


s = "barfoothefoobarman"
words = ["foo", "bar"]
sol = Solution()
print(sol.findSubstring(s, words))
