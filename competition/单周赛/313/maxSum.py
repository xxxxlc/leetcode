
# 给你一个大小为 m x n 的整数矩阵 grid 。

# 按以下形式将矩阵的一部分定义为一个 沙漏 ：
# 返回沙漏中元素的 最大 总和。

# 注意：沙漏无法旋转且必须整个包含在矩阵中。


class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        maxSum = 0

        for i in range(0, m - 2):
            for j in range(0, n - 2):
                ksum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                maxSum = max(ksum, maxSum)
        
        return maxSum
                


grid = [[1,2,3],[4,5,6],[7,8,9]]


a = Solution()
print(a.maxSum(grid))
