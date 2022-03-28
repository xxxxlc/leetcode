# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zerosindex = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zerosindex.append([i, j])
        
        for idx in zerosindex:
            row = idx[0]
            col = idx[1]

            for i in range(n):
                matrix[row][i] = 0
            for i in range(m):
                matrix[i][col] = 0
        
        return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

a = Solution()
print(a.setZeroes(matrix))