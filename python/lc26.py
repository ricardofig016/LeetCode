class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        nums.sort()
        aux = [nums[0]]
        for i in nums:
            if i != aux[-1]:
                aux.append(i)
                k += 1
        for i in range(k):
            nums[i] = aux[i]

        return k


nums = [1, 1, 2]
s = Solution()
k = s.removeDuplicates(nums)
print("k:", k)
for i in nums:
    print(i)
