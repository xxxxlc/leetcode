# Alice 和 Bob 用几堆石子在做游戏。几堆石子排成一行，每堆石子都对应一个得分，由数组 stoneValue 给出。

# Alice 和 Bob 轮流取石子，Alice 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子 。比赛一直持续到所有石头都被拿走。

# 每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 0 。比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。

# 假设 Alice 和 Bob 都采取 最优策略 。如果 Alice 赢了就返回 "Alice" ，Bob 赢了就返回 "Bob"，平局（分数相同）返回 "Tie" 。
from modulefinder import STORE_NAME


class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        # a = [0] * (n + 1)
        # b = [0] * (n + 1)
        dp = [0] * (n + 1)
        temp = 0
        for i in range(n - 1, -1, -1):
            temp = temp + stoneValue[i]
            # a[i] = sum(stoneValue[i:]) - b[i + 1]
            # b[i] = sum(stoneValue[i:]) - a[i + 1]
            dp[i] = temp - dp[i + 1]
            for x in range(2, 4):
                if i + x <= n:
                    # a[i] = max(a[i], sum(stoneValue[i:]) - b[i + x])
                    # b[i] = max(b[i], sum(stoneValue[i:]) - a[i + x])
                    dp[i] = max(dp[i], temp - dp[i + x])
        print(dp[0])
        if dp[0] > temp - dp[0]:
            return 'Alice'
        elif dp[0] == temp - dp[0]:
            return 'Tie'
        else:
            return 'Bob'




values =[1,2,3,-1,-2,-3,7]
a = Solution()
print(a.stoneGameIII(values))