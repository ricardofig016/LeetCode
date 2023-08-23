class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        if s == t:
            return t
        a = 0
        b = 1
        window = ""
        best_wind = ""
        while b > a:
            print(f"window: {window}\nbest_wind: {best_wind}")
            window = s[a:b]
            copy = window[:]
            for ch in t:
                t_in_wind = True
                if ch in copy:
                    copy = copy.replace(ch, "", 1)
                else:
                    t_in_wind = False
                    break
                print(f"copy: {copy}")
            if t_in_wind:
                if best_wind == "" or len(window) < len(best_wind):
                    best_wind = window
                if window == n:
                    return window
                a += 1
            else:
                if b == m:
                    return best_wind
                b += 1
        return best_wind


s = "bbaa"
t = "aba"
sol = Solution()
print("solution: ", sol.minWindow(s, t))
