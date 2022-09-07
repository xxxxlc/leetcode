# 我们正在玩一个猜数游戏，游戏规则如下：

# 我从 1 到 n 之间选择一个数字。
# 你来猜我选了哪个数字。
# 如果你猜到正确的数字，就会 赢得游戏 。
# 如果你猜错了，那么我会告诉你，我选的数字比你的 更大或者更小 ，并且你需要继续猜数。
# 每当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。如果你花光了钱，就会 输掉游戏 。
# 给你一个特定的数字 n ，返回能够 确保你获胜 的最小现金数，不管我选择那个数字 。


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n-1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = j + dp[i][j - 1]
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))
        
        return dp[1][n]


n = 10

a = Solution()
print(a.getMoneyAmount(n))