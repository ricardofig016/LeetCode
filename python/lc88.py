class Solution(object):
    def merge(self, nums1, m, nums2, n):
        next1 = 0
        next2 = 0
        aux = []
        while next1 < m and next2 < n:
            if nums1[next1] > nums2[next2]:
                aux.append(nums2[next2])
                next2 += 1
            else:
                aux.append(nums1[next1])
                next1 += 1

        while next1 < m:
            aux.append(nums1[next1])
            next1 += 1

        while next2 < n:
            aux.append(nums2[next2])
            next2 += 1

        for i in range(n + m):
            nums1[i] = aux[i]

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
s = Solution()
s.merge(nums1, m, nums2, n)
for i in nums1:
    print(i)
