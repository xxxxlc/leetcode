# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内

import math

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nth = 0
        number = 1
        # d = []
        while(nth < n):
            array = self.getArray(number)
            isPrimes = all(i in primes for i in array)
            if isPrimes:
                nth += 1
                # d.append(number)
            number += 1
        return number - 1


    def getArray(self, n):
        if n == 1:
            return []
        if self.isPrime(n):
            primeArray = [n]
        else:
            primeArray = []
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    if self.isPrime(i):
                        primeArray.append(i)
                    if self.isPrime(n / i):
                        primeArray.append(n / i)
        return primeArray

    def isPrime(self, i):
        return all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1))

n = 12
primes = [2,7,13,19]

a = Solution()
print(a.nthSuperUglyNumber(n, primes))
