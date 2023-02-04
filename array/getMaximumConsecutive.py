# 给你一个长度为 n 的整数数组 coins ，它代表你拥有的 n 个硬币。第 i 个硬币的值为 coins[i] 。如果你从这些硬币中选出一部分硬币，它们的和为 x ，那么称，你可以 构造 出 x 。

# 请返回从 0 开始（包括 0 ），你最多能 构造 出多少个连续整数。

# 你可能有多个相同值的硬币。

from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:

        coins.sort()

        x = 0

        for i in range(len(coins)):
            if coins[i] <= x + 1:
                x += coins[i]
            else:
                break
        
        return x + 1


coins = [1,4,10,3,1]

a = Solution()
print(a.getMaximumConsecutive(coins))
