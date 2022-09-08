# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

# 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0

        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    increasement = 4
                    for d in direction:
                        x = d[0] + row 
                        y = d[1] + col
                        if 0 <= x < m and 0 <= y < n:
                            if grid[x][y] == 1:
                                increasement -= 1
                    ans += increasement
        
        return ans

                


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

a = Solution()
print(a.islandPerimeter(grid))
