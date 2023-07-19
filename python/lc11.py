class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        best_area = 0
        left = 0
        right = n - 1
        while right > left:
            area = min(height[left], height[right]) * (right - left)
            best_area = max(best_area, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return best_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
s = Solution()
print(s.maxArea(height))
