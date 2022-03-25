# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        left = 0
        right = m

        while (left < right):
            mid = left + (right - left) // 2
            if matrix[mid][n] == target:
                return True
            elif matrix[mid][n] < target:
                left = mid + 1
            elif matrix[mid][n] > target:
                right = mid
        
        depth = left
        left = 0
        right = n

        while (left <= right):
            mid = left + (right - left) // 2
            if matrix[depth][mid] == target:
                return True
            elif matrix[depth][mid] < target:
                left = mid + 1
            elif matrix[depth][mid] > target:
                right = mid - 1
        
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

a = Solution()
print(a.searchMatrix(matrix, target))