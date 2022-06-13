# 给你两个大小为 n x n 的二进制矩阵 mat 和 target 。现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        for i in range(4):
            if self.isequal(mat, target):
                return True
            mat = self.rotate(mat)
        return False
    
    def rotate(self, matrix):
        row = len(matrix) - 1
        col = len(matrix[0]) - 1 

        for i in range(0, (row + 1) // 2):
            for j in range(0, (col + 2)// 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[col - j][i]
                matrix[col - j][i] = matrix[col - i][col - j]
                matrix[col - i][col - j] = matrix[j][col - i]
                matrix[j][col - i] = temp
        return matrix
    
    def isequal(self, a, b):
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] != b[i][j]:
                    return False
        return True


mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]

a = Solution()
print(a.findRotation(mat, target))
