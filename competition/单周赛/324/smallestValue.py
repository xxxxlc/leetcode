# 给你一个正整数 n 。

# 请你将 n 的值替换为 n 的 质因数 之和，重复这一过程。

# 注意，如果 n 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。
# 返回 n 可以取到的最小值。


class Solution(object):
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """

        while True:
            x = sum(self.getPrime(int(n)))
            if n == x:
                break
            else:
                n = x
        
        return n
        
    

    def getPrime(self, x):
        primeArray = []
        while(x != 1):
            for i in range(2, int(x+1)):
                while x % i == 0:
                    x = x / i
                    primeArray.append(i)
                if x == 1:
                    break
        
        return primeArray

n = 15

a = Solution()
print(a.smallestValue(n))