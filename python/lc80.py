class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag1 = []  # numbers that have appeared once
        flag2 = []  # numbers that have appeared twice
        k = 0
        aux = []
        for i in nums:
            if i in flag1:
                aux.append(i)
                k += 1
                flag1.remove(i)
                flag2.append(i)
            elif i in flag2:
                pass
            else:
                aux.append(i)
                k += 1
                flag1.append(i)

        for i in range(k):
            nums[i] = aux[i]

        return k


nums = [1, 1, 2]
s = Solution()
k = s.removeDuplicates(nums)
print("k:", k)
for i in nums:
    print(i)
