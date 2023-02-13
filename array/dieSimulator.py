# 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

# 不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。

# 现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。

# 假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果

from functools import lru_cache
from typing import List

class Solution:
    # 超时
    # def dieSimulator(self, n: int, rollMax: List[int]) -> int:
    #     self.MOD = 10 ** 9 + 7
    #     self.ans = 0
    #     self.n = n
    #     self.rollMax = rollMax

    #     self.trackback([], -1, 0)

    #     return self.ans


    # def trackback(self, track, number, num):
    #     if len(track) == self.n:
    #         self.ans = (self.ans + 1) % self.MOD
    #         return 

    #     for i in range(1, 7):
    #         if i != number:
    #             self.trackback(track + [i], i, 1)
    #         elif num < self.rollMax[number - 1]:
    #             self.trackback(track + [i], i, num + 1)

    # 记忆化搜索
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, j, x):
            if i >= n:
                return 1
            ans = 0

            for k in range(1, 7):
                if k != j:
                    ans += dfs(i + 1, k, 1)
                elif x < rollMax[k - 1]:
                    ans += dfs(i + 1, k, x + 1)
            
            return ans % (10 ** 9 + 7)
        
        return dfs(0, 0, 0)



n = 2
rollMax = [1,1,2,2,2,3]

a = Solution()
print(a.dieSimulator(n, rollMax))