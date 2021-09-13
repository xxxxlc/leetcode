
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
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
                


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
a = Solution()
print(a.rotate(matrix))