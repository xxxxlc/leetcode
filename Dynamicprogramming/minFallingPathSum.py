# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        while len(matrix) >= 2:
            row = matrix.pop()
            for i in range(len(row)):
                matrix[-1][i] += min(row[max(0, i - 1):min(len(row), i + 2)])
        return min(matrix[0])


matrix = [[2,1,3],[6,5,4],[7,8,9]]

a = Solution()
print(a.minFallingPathSum(matrix))
