# 石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，爱丽丝先开始 。

# 有 n 块石子排成一排。每个玩家的回合中，可以从行中 移除 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 和 相等的得分。当没有石头可移除时，得分较高者获胜。

# 鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 减小得分的差值 。爱丽丝的目标是最大限度地 扩大得分的差值 。

# 给你一个整数数组 stones ，其中 stones[i] 表示 从左边开始 的第 i 个石头的值，如果爱丽丝和鲍勃都 发挥出最佳水平 ，请返回他们 得分的差值 。

class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        sumstone = [[0 for _ in range(n)] for _ in range(n)]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(0, n):
            for j in range(i, n):
                if i == j:
                    sumstone[i][j] = stones[i]
                else:
                    sumstone[i][j] = stones[j] + sumstone[i][j - 1]
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(sumstone[i + 1][j] - dp[i + 1][j], sumstone[i][j - 1] - dp[i][j - 1])
        
        return dp[0][n - 1]





stones = [5,3,1,4,2]

a = Solution()
print(a.stoneGameVII(stones))