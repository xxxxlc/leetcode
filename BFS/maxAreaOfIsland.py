# 给你一个大小为 m x n 的二进制矩阵 grid 。

# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

# 岛屿的面积是岛上值为 1 的单元格的数目。

# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        maxarea = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if visit[i][j] == 1 or grid[i][j] == 0:
                    continue
                else:
                    q = []
                    q.append([i, j])
                    visit[i][j] = 1

                    area = 1

                    while(q):
                        cur = q.pop(0)

                        for d in directions:
                            x = cur[0] + d[0]
                            y = cur[1] + d[1]

                            if len(grid) > x >= 0 and len(grid[0]) > y >= 0 and grid[x][y] == 1 and visit[x][y] == 0:
                                q.append([x, y])
                                area += 1
                                visit[x][y] = 1
                    
                    if area > maxarea:
                        maxarea = area
        
        return maxarea
                                 




grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

a = Solution()
print(a.maxAreaOfIsland(grid))