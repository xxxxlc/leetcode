# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

# 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。

# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。

# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。


class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]

        i = 0
        j = 0

        for row in range(m):
            for col in range(n):
                if j == c:
                    i += 1
                    j = 0
                ans[i][j] = mat[row][col]

                j += 1
        
        return ans
                

mat = [[1,2],[3,4]]
r = 4
c = 1

a = Solution()
print(a.matrixReshape(mat, r, c))