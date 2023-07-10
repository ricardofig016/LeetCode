class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        if sum(diff) < 0:
            return -1

        total = 0
        start = 0
        for i in range(n):
            total += diff[i]
            if total < 0:
                total = 0
                start = i + 1
        return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
s = Solution()
print(s.canCompleteCircuit(gas, cost))
