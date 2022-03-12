# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。

# 如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。

# 请你返回 grid2 中 子岛屿 的 数目 。

from matplotlib.pyplot import grid


class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        ans = 0
        visited = [[0 for _ in range(len(grid1[0]))] for _ in range(len(grid1))]
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    issubisland = True

                    if grid1[i][j] == 0:
                        issubisland = False 

                    q = []
                    q.append([i, j])

                    while(q):
                        size = len(q)

                        for k in range(size):
                            cur = q.pop(0)

                            for d in direction:
                                x = cur[0] + d[0]
                                y = cur[1] + d[1]

                                if 0 <= x < len(grid1) and 0 <= y < len(grid1[0]) and grid2[x][y] == 1 and visited[x][y] == 0:
                                    visited[x][y] = 1
                                    if grid1[x][y] == 0:
                                        issubisland = False
                                    q.append([x, y])
                    
                    if issubisland:
                        ans += 1
        return ans



grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

a = Solution()
print(a.countSubIslands(grid1, grid2))


