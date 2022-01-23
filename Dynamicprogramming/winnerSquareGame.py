# Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。

# 一开始，有 n 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 任意 非零 平方数 个石子。

# 如果石子堆里没有石子了，则无法操作的玩家输掉游戏。

# 给你正整数 n ，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回 True ，否则返回 False 。



class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [0] * (n + 1)
        dp[-1] = 0
        
        for i in range(n - 1, -1, -1):
            j = 1
            while(j ** 2 <= n - i):
                if not dp[i + j ** 2]:
                    dp[i] = 1
                j = j + 1
        if dp[0]:
            return True
        else:
            return False

n = 7
a = Solution()
print(a.winnerSquareGame(n))