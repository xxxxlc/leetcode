# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_primes = [True] * n
        result = 0
        for i in range(2, n):
            # 如果当前值是素数，就将它倍数标记为合数
            if is_primes[i]:
                result += 1
                _power = i * i
                if _power < n :
                    for j in range(_power, n, i):
                        is_primes[j] = False
        return result

n = 10

a = Solution()
print(a.countPrimes(n))