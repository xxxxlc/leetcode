# 泰波那契序列 Tn 定义如下： 

# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * (n + 1)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a[0] = 0
        a[1] = 1
        a[2] = 1
        for i in range(3, n + 1):
            a[i] = a[i-1] + a[i-2] + a[i-3]
        
        return a[n]
        


n = 25
a = Solution()
print(a.tribonacci(n))