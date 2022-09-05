# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。

class Solution(object):
    map = dict()
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.map:
            return self.map[n]

        if n == 0:
            self.map[0] = 1
            return 1
        if n == 1:
            self.map[1] = 10
            return 10
        ans = 1
        for i in range(n):
            if i == 0:
                ans *= 9
            else:
                ans *= 10 - i
        ans += self.countNumbersWithUniqueDigits(n - 1)
        
        return ans


n = 3

a = Solution()
print(a.countNumbersWithUniqueDigits(n))