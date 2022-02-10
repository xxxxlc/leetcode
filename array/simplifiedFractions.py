# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回。


class Solution(object):
    ans = dict()
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            self.ans[n] = []
            return self.ans[n]
        if n in self.ans:
            return self.ans[n]

        res = []
        for i in range(1, n):
            if self.common_factor(i, n) or i == 1:
                res.append(str(i) + '/' + str(n))
        
        return self.simplifiedFractions(n - 1) + res
    
    def common_factor(self, x, y):
        if y % x == 0:
            return False
        for i in range(2, x):
            if x % i == 0 and y % i == 0:
                return False
        
        return True

        


n = 4

a = Solution()
print(a.simplifiedFractions(n))