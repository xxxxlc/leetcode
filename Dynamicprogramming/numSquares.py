# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        squares = []
        while(i ** 2 <= n):
            squares.append(i ** 2)
            i = i + 1
        
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - square])
        if dp[n - 1] == n:
            return n
        return dp[n]



n = 12

a = Solution()
print(a.numSquares(n))