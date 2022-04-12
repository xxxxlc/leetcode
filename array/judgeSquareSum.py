# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        n = int(math.sqrt(c)) + 1
        return any(math.sqrt(c - i * i) == int(math.sqrt(c - i * i)) for i in range(n))
        # for i in range(n):
        #     if math.sqrt(c - i * i) == int(math.sqrt(c - i * i)):
        #         return True
        # return False


c = 6

a = Solution()
print(a.judgeSquareSum(c))