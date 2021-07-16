# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

# 选出任一 x，满足 0 < x < N 且 N % x == 0 。
# 用 N - x 替换黑板上的数字 N 。
# 如果玩家无法执行这些操作，就会输掉游戏。

# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False。假设两个玩家都以最佳状态参与游戏。


class Solution(object):
    map = dict()
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in self.map:
            return self.map[n]
        self.map[1] = False
        for i in range(2, n + 1):
            self.map[i] = True
            for j in (1, i//2):
                if i % j == 0:
                    self.map[i] = self.map[i - j] and self.map[i]
            self.map[i] = not self.map[i]
        
        return self.map[n]


n = 8
a = Solution()
print(a.divisorGame(n))