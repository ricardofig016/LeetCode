class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans1 = [1] * n
        for i in range(1, n):
            ans1[i] = ans1[i - 1] * nums[i - 1]

        ans2 = [1] * n
        for i in reversed(range(n - 1)):
            ans2[i] = ans2[i + 1] * nums[i + 1]

        answer = [ans1[i] * ans2[i] for i in range(n)]
        return answer


nums = [1, 2, 3, 4]
s = Solution()
print(s.productExceptSelf(nums))
