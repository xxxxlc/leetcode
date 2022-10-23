# 给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。

# 你可以执行下面操作 任意 次：

# 将 nums 中 任意 元素增加或者减小 1 。
# 对第 i 个元素执行一次操作的开销是 cost[i] 。

# 请你返回使 nums 中所有元素 相等 的 最少 总开销。

class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        a = sorted(zip(nums, cost))
        mid = sum(cost) // 2
        s = 0
        for x, c in a:
            s += c

            if s > mid:
                return sum(abs(y - x) * c for y, c in a)


nums = [1,3,5,2]
cost = [2,3,1,14]

a = Solution()
print(a.minCost(nums, cost))