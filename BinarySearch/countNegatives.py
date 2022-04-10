# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 请你统计并返回 grid 中 负数 的数目。

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[-1][-1] >= 0:
            return 0
        m = len(grid)
        n = len(grid[0])

        ans = 0

        for i in range(m):
            if grid[i][0] < 0:
                return m * n - ans
            
            left = 0
            right = n

            if grid[i][n - 1] >= 0:
                ans += n
                continue

            while (left < right):
                mid = left + (right - left) // 2

                if grid[i][mid] < 0 and grid[i][mid - 1] >= 0:
                    ans += mid 
                    break
                elif grid[i][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid
        
        return m * n - ans




grid = [[4,3,3,1,1],[1,0,0,-1,-1],[-2,-2,-2,-2,-3],[-2,-2,-2,-3,-3],[-3,-3,-3,-3,-3]]

a = Solution()
print(a.countNegatives(grid))