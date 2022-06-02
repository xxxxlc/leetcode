# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        m = len(mat)
        ans = 0
        
        for i in range(0, m):
            ans += mat[i][i]
            ans += mat[i][m-i-1]
        
        if m % 2 == 0:
            return ans
        else:
            return ans - mat[m // 2][m // 2]

mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]

a = Solution()
print(a.diagonalSum(mat))