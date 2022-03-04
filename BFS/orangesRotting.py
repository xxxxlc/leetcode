# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 

from time import time


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visited[i][j] = 1
                if grid[i][j] == 0:
                    visited[i][j] = 1
        if not q:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            return 0
        time = 0
        while(q):
            time += 1

            for k in range(len(q)):
                cur = q.pop(0)

                for d in directions:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visited[x][y] == 0:
                        q.append([x, y])
                        visited[x][y] = 1
                        grid[x][y] = 2
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time - 1

grid = [[2,1,1],[1,1,0],[0,1,1]]

a = Solution()
print(a.orangesRotting(grid))