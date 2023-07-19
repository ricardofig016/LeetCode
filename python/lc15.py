class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = set()
        for first in range(len(nums)):
            if nums[first] > 0:
                break
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while third > second:
                sum = nums[first] + nums[second] + nums[third]
                if sum == 0:
                    triplets.add((nums[first], nums[second], nums[third]))
                    second += 1
                    third -= 1
                elif sum < 0:
                    second += 1
                else:
                    third -= 1

        return list(triplets)


nums = [-2, -1, -1, 0, 1, 1, 2]
s = Solution()
print(s.threeSum(nums))
