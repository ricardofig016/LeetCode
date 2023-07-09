class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]


nums = [3, 2, 3]
s = Solution()
print(s.majorityElement(nums))
