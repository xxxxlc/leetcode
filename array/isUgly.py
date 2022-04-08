# 丑数 就是只包含质因数 2、3 和 5 的正整数。

# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。


class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n % 2 == 0):
            n = n / 2
        
        while (n % 5 == 0):
            n = n / 5
        
        while (n % 3 == 0):
            n = n / 3
        
        return n == 1


n = 14

a = Solution()
print(a.isUgly(n))