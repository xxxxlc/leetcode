# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 和一个整数 k 。你从起点 (0, 0) 出发，每一步只能往 下 或者往 右 ，你想要到达终点 (m - 1, n - 1) 。

# 请你返回路径和能被 k 整除的路径数目，由于答案可能很大，返回答案对 109 + 7 取余 的结果

from functools import cache


MOD = 10 ** 9 + 7

class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, v):
            if i < 0 or j < 0:
                return 0
            v = (v + grid[i][j]) % MOD
            if i == j == 0: return v == 0
            return (dfs(i - 1, j, v) + dfs(i, j - 1, v)) % MOD
        
        ans = dfs(m - 1, n - 1, 0)
        dfs.cache_clear()
        return int(ans)


grid = [[5,2,4],[3,0,5],[0,7,2]]
k = 3

a = Solution()
print(a.numberOfPaths(grid))