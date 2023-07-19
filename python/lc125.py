class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(ch for ch in s if ch.isalnum()).lower()

        left = 0
        right = len(s) - 1
        while right > left:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


string = "A man, a plan, a canal: Panama"
s = Solution()
print(s.isPalindrome(string))
