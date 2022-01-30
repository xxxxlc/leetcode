# Alice 和 Bob 玩一个游戏，两人轮流操作， Alice 先手 。

# 总共有 n 个石子排成一行。轮到某个玩家的回合时，如果石子的数目 大于 1 ，他将执行以下操作：

# 选择一个整数 x > 1 ，并且 移除 最左边的 x 个石子。
# 将 移除 的石子价值之 和 累加到该玩家的分数中。
# 将一个 新的石子 放在最左边，且新石子的值为被移除石子值之和。
# 当只剩下 一个 石子时，游戏结束。

# Alice 和 Bob 的 分数之差 为 (Alice 的分数 - Bob 的分数) 。 Alice 的目标是 最大化 分数差，Bob 的目标是 最小化 分数差。

# 给你一个长度为 n 的整数数组 stones ，其中 stones[i] 是 从左边起 第 i 个石子的价值。请你返回在双方都采用 最优 策略的情况下，Alice 和 Bob 的 分数之差 。




class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        dp = [0] * n
        pre = [0] * n
        pre[0] = stones[0]
        for i in range(1, n):
            pre[i] = stones[i] + pre[i - 1]
        
        dp[n - 1] = pre[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], pre[i] - dp[i + 1])
        
        return dp[1]



stones = [-1,2,-3,4,-5]

a = Solution()
print(a.stoneGameVIII(stones))