class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        water_left = [0] * n
        water_right = [0] * n

        for i in range(1, n - 1):
            water_left[i] = max(water_left[i - 1], height[i - 1])
        water_left[n - 1] = 0

        for i in reversed(range(1, n - 1)):
            water_right[i] = max(water_right[i + 1], height[i + 1])
        water_right[n - 1] = 0

        max_water = [min(water_left[i], water_right[i]) for i in range(n)]

        water_sum = 0
        for i in range(n):
            water_sum += max(0, max_water[i] - height[i])

        return water_sum


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap(height))
