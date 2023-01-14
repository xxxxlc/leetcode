# 给你一个由正整数组成的数组 nums 。

# 数字序列的 最大公约数 定义为序列中所有整数的共有约数中的最大整数。

# 例如，序列 [4,6,16] 的最大公约数是 2 。
# 数组的一个 子序列 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。

# 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
# 计算并返回 nums 的所有 非空 子序列中 不同 最大公约数的 数目 。

from typing import List
from math import gcd


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        ans, mx = 0, max(nums)

        has = [False] * (mx + 1)

        for x in nums: 
            has[x] = True
            ans += 1

        for i in range(1, mx // 3 + 1):
            
            if has[i]: continue

            g = 0

            for j in range(i * 2, mx + 1, i):
                if has[j]:
                    g = gcd(g, j)

                    if g == i:
                        ans += 1

                        break
        
        return ans



nums = [6,10,3]

a = Solution()
print(a.countDifferentSubsequenceGCDs(nums))