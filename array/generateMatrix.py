# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        i = 0
        j = 0
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        num = 1
        d = 0

        while (num <= n ** 2):
            matrix[i][j] = num
            num += 1

            if i + direction[d][0] >= n or j + direction[d][1] >= n:
                d = (d + 1) % 4
            if matrix[i + direction[d][0]][j + direction[d][1]] != 0:
                d = (d + 1) % 4
            
            i += direction[d][0]
            j += direction[d][1]

        return matrix
            



            

n = 2

a = Solution()
print(a.generateMatrix(n))