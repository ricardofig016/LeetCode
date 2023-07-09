class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        aux = []
        for i in nums:
            if i != val:
                k += 1
                aux.append(i)

        for i in range(k):
            nums[i] = aux[i]

        return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
s = Solution()
k = s.removeElement(nums, val)
print("k:", k)
for i in nums:
    print(i)
