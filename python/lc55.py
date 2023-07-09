class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_pos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last_pos:
                last_pos = i

        return last_pos == 0


nums = [2, 3, 1, 1, 4]
s = Solution()
print(s.canJump(nums))
