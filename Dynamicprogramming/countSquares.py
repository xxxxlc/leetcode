# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        dp = [[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]

        s = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    elif matrix == 0:
                        dp[row][col] = 0
                    else:
                        dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    s += dp[row][col]
        
        return s

a = Solution()

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(a.countSquares(matrix))