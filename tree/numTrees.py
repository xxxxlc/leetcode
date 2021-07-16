# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

import Bintree
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1)/(i + 2)
        return int(C)


n = 3
a = Solution()
print(a.numTrees(n))


