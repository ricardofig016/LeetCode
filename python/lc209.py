class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        best_size = n + 1
        s, e = (0, 0)
        curr_window_sum = nums[0]
        while s < n and e < n:
            if curr_window_sum < target:
                e += 1
                if e < n:
                    curr_window_sum += nums[e]
            else:
                best_size = min(best_size, e - s + 1)
                if best_size == 1:
                    return best_size
                curr_window_sum -= nums[s]
                s += 1
        return 0 if best_size == n + 1 else best_size


target = 7
nums = [2, 3, 1, 2, 4, 3]
s = Solution()
print(s.minSubArrayLen(target, nums))
