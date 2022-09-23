# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。

# 你必须找到一个内存复杂度优于 O(n2) 的解决方案。

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left = matrix[0][0]
        right = matrix[-1][-1]
        n = len(matrix)

        while(left < right):
            mid = (right - left) // 2 + left

            num = 0
            i = n - 1
            j = 0
            while(i >= 0 and j < n):
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            
            if num >= k:
                right = mid
            else:
                left = mid + 1
            
        return left


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

a = Solution()
print(a.kthSmallest(matrix, k))