# 给定一个整数 n ，返回 n! 结果中尾随零的数量。

# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        num2 = 0
        num5 = 0
        for i in range(1, n + 1):
            cur = i
            while(cur % 2 == 0):
                cur = cur // 2
                num2 += 1
            while(cur % 5 == 0):
                cur = cur // 5
                num5 += 1
        return min(num2,num5)

n = 5

a = Solution()
print(a.trailingZeroes(n))