# 给你一个正整数 n ，找出满足下述条件的 中枢整数 x ：

# 1 和 x 之间的所有元素之和等于 x 和 n 之间所有元素之和。
# 返回中枢整数 x 。如果不存在中枢整数，则返回 -1 。题目保证对于给定的输入，至多存在一个中枢整数。


class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1


        for i in range(1, n):
            tot1 = (1 + i) * i // 2
            tot2 = (i + n) * (n - i + 1) // 2

            if tot1 == tot2:
                return i
        
        return -1


a = Solution()
n = 8
print(a.pivotInteger(n))

 