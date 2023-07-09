class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_infinity = 10**4 + 1
        n = len(nums)
        if n == 1:
            return 0
        aux = [0] * n
        index = n - 2
        while index >= 0:
            best_jump = pos_infinity
            for j in range(index + 1, index + nums[index] + 1):
                if j >= n:
                    break
                best_jump = min(best_jump, aux[j])
            aux[index] = best_jump + 1
            index -= 1
        return aux[0]


nums = [2, 3, 1, 1, 4]
nums2 = [2, 1]
s = Solution()
print(s.jump(nums2))
