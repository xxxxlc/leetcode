# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return list()

        m, n = len(matrix), len(matrix[0])
        ans = []

        left, right, top, bottom = 0, n - 1, 0, m - 1

        while (left <= right and top <= bottom):
            ans.extend(matrix[top][column] for column in range(left, right + 1))
            ans.extend(matrix[row][right] for row in range(top + 1, bottom + 1))

            if left < right and top < bottom:
                ans.extend(matrix[bottom][column] for column in range(right - 1, left, -1))
                ans.extend(matrix[row][left] for row in range(bottom, top, -1))
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        
        return ans




matrix = [[1,2,3],[4,5,6],[7,8,9]]

a = Solution()
print(a.spiralOrder(matrix))