# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

import math

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        ans = int(math.log(n) / math.log(4))
        return pow(4, ans) == n or pow(4, ans + 1) == n

a = Solution()
print(a.isPowerOfFour(17))


