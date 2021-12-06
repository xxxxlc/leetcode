# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def quickMul(N):
            ans = 1
            contribute = x

            while(N > 0):
                if N % 2 == 1:
                    ans *= contribute
                contribute *= contribute
                N = N // 2
            
            return ans

        if n >= 0:
            return quickMul(n)
        else:
            return 1.0 / quickMul(-n)


x = 2
n = 10

a = Solution()
print(a.myPow(x, n))