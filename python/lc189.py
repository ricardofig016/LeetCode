class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        aux = nums[-k:]
        aux += nums[: n - k]
        for i in range(n):
            nums[i] = aux[i]


nums = [1, 2, 3, 4, 5, 6]
k = 1
s = Solution()
s.rotate(nums, k)
for i in nums:
    print(i)
