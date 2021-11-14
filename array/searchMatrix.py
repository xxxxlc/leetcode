# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            idx = self.search(row, target)
            if idx > 0:
                return True
        return False
    
    def search(self, row, target):
        left = 0
        right = len(row) - 1
        if target > row[right]:
            return -1
        while(left <= right):
            mid = (right - left) // 2 + left
            if target == row[mid]:
                return 1
            elif target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
        return -1 




matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

a = Solution()
print(a.searchMatrix(matrix, target))
