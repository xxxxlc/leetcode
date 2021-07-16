# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。


class Solution(object):
    def __init__(self):
        pass
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        stair = len(cost)
        min_cost = [0]*stair
        min_cost[1] = min(cost[0], cost[1])
        for i in range(2, stair):
            min_cost[i] = min(min_cost[i - 2] + cost[i - 1], min_cost[i - 1] + cost[i])
        return min_cost[-1]



cost = [0,2,2,1]
a = Solution()
print(a.minCostClimbingStairs(cost))