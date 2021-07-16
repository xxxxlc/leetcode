# 斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        a1 = 0
        a2 = 1
        for i in range(1, n):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
        return a2


a = Solution()
n = 4
print(a.fib(n))