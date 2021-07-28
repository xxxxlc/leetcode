# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

# 说明: 

# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        sumGas = 0
        for i in range(0, n):
            sumGas += gas[i] - cost[i]

        if sumGas < 0:
            return -1

        tank = 0
        start = 0

        for i in range(0, n):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        
        if start == n:
            return 0
        
        return start
        



gas = [2,3,4]
cost = [3,4,3]

a = Solution()
print(a.canCompleteCircuit(gas, cost))
