# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。


import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = math.floor(math.sqrt(2 * n))

        if ans * (ans + 1) > 2 * n:
            return int(ans - 1)
        else:
            return int(ans)


n = 8

a = Solution()
print(a.arrangeCoins(n))