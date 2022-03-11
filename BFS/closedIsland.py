# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

# 请返回 封闭岛屿 的数目。


class Solution(object):
    def closedIsland(self, grid):
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

                if grid[i][j] == 1:
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

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and visited[x][y] == 0:
                        q.append([x, y])
                        visited[x][y] = 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and visited[i][j] == 0:
                    ans += 1
                    q = []
                    q.append([i, j])

                    while(q):
                        size = len(q)

                        for k in range(size):
                            cur = q.pop(0)

                            for d in direction:
                                x = cur[0] + d[0]
                                y = cur[1] + d[1]

                                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and visited[x][y] == 0:
                                    q.append([x, y])
                                    visited[x][y] = 1
        
        return ans


                     
                        
 
grid = [[0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]



a = Solution()
print(a.closedIsland(grid))
