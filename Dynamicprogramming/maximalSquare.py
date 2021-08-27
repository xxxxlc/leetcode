# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        dp = [[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]

        maxside = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                    maxside = max(maxside, dp[row][col])
        
        return maxside * maxside
        
        


a = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(a.maximalSquare(matrix))