# 亚历克斯和李继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。

# 亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。

# 在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。

# 游戏一直持续到所有石子都被拿走。

# 假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头

from numpy import place
from sympy import solve


class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        dp = [[0 for _ in range(0, n)] for _ in range(0, n)]

        
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if 2 * m >= n - i:
                    dp[i][m - 1] = sum(piles[i:])
                else:
                    for x in range(1, 2 * m + 1):
                        if i + x < n:
                            dp[i][m - 1] = max(dp[i][m - 1], sum(piles[i:]) - dp[i + x][max(x, m) - 1])
        return dp[0][0]





piles = [2,7,9,4,4]
a = Solution()
print(a.stoneGameII(piles))