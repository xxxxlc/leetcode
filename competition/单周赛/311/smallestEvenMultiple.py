
# 给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 != 0:
            return 2 * n
        
        else:
            return n


n = 5

a = Solution()
print(a.smallestEvenMultiple(n))