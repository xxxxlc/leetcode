# 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        time = 1
        sums = 0

        while (n != 0):
            d = n % 10
            n = n // 10
            time *= d
            sums += d
        
        return time - sums

n = 234

a = Solution()
print(a.subtractProductAndSum(n))