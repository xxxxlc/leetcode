# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

# i - k <= r <= i + k,
# j - k <= c <= j + k 且
# (r, c) 在矩阵内。

class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        self.p = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ans = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.p[i][j] = self.p[i - 1][j] + self.p[i][j - 1] - self.p[i - 1][j - 1] + mat[i - 1][j - 1]
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = self.get(i + k + 1, j + k + 1, m, n) - \
                            self.get(i - k, j + k + 1, m, n) - \
                            self.get(i + k + 1, j - k, m, n) + \
                            self.get(i - k, j - k, m, n)
        return ans
    
    def get(self, x, y, m, n):
        x = max(min(x, m), 0)
        y = max(min(y, n), 0)

        return self.p[x][y]

mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 2

a = Solution()
print(a.matrixBlockSum(mat, k))