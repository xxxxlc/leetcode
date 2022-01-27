# Alice 和 Bob 轮流玩一个游戏，Alice 先手。

# 一堆石子里总共有 n 个石子，轮到某个玩家时，他可以 移出 一个石子并得到这个石子的价值。Alice 和 Bob 对石子价值有 不一样的的评判标准 。双方都知道对方的评判标准。

# 给你两个长度为 n 的整数数组 aliceValues 和 bobValues 。aliceValues[i] 和 bobValues[i] 分别表示 Alice 和 Bob 认为第 i 个石子的价值。

# 所有石子都被取完后，得分较高的人为胜者。如果两个玩家得分相同，那么为平局。两位玩家都会采用 最优策略 进行游戏。

# 请你推断游戏的结果，用如下的方式表示：

# 如果 Alice 赢，返回 1 。
# 如果 Bob 赢，返回 -1 。
# 如果游戏平局，返回 0 。

class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        n = len(aliceValues)
        nums = [0] * n
        for i in range(0, n):
            nums[i] = [aliceValues[i] + bobValues[i], i]
        nums = sorted(nums, key=lambda x: x[0], reverse=True)
        alicescore = 0
        bobscore = 0

        for i in range(0, n):
            if i % 2 == 0:
                alicescore += aliceValues[nums[i][1]]
            else:
                bobscore += bobValues[nums[i][1]]
        if alicescore > bobscore:
            return 1
        elif alicescore < bobscore:
            return -1
        else:
            return 0






aliceValues = [1,2]
bobValues = [3,1]

a = Solution()
print(a.stoneGameVI(aliceValues, bobValues))