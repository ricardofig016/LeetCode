class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ptr = 0
        t_ptr = 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
        return s_ptr == len(s)


s = "abc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))
