# 给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。

# 给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 109 + 7 取余 的结果。

# 如果所执行移动的顺序不完全相同，则认为两种方法不同。

# 注意：数轴包含负整数


class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        if abs(endPos - startPos) > k:
            return 0
        
        n = abs(endPos - startPos)

        if (k - n) % 2 != 0:
            return 0


        k_fac = 1
        n_fac = 1
        m_fac = 1
        for i in range(1, k + 1):
            k_fac *= i

        for i in range(1, n  + (k - n) // 2 + 1):
            n_fac *= i
        
        for i in range(1, (k - n) // 2 + 1):
            m_fac *= i
        
        return int(k_fac / n_fac // m_fac) % (10 ** 9 + 7)
        


startPos = 671
endPos = 669
k = 4

a = Solution()
print(a.numberOfWays(startPos, endPos, k))