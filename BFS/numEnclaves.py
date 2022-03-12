# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        q = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 0:
                    pass
                else:
                    if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                        visited[i][j] = 1
                        q.append([i, j])
        
        while(q):
            size = len(q)

            for k in range(size):
                cur = q.pop(0)

                for d in direction:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and visited[x][y] == 0:
                        q.append([x, y])
                        visited[x][y] = 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    ans += 1
                    
        
        return ans


grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]



a = Solution()
print(a.numEnclaves(grid))