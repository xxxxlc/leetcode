# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        for i in range(0, n + 1):
            ans[i] = self.countOnes(i)
        
        return ans
    
    def countOnes(self, x):
        ones = 0
        while(x > 0):
            x = x & (x - 1)
            ones += 1
        return ones



n = 5
a = Solution()
print(a.countBits(n))