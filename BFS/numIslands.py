# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        map = [[0 for _ in range(0, len(grid[0]))] for j in range(len(grid))]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if map[i][j] == 0 and grid[i][j] == '1':
                    map[i][j] = 1
                    ans += 1
                    q = []
                    q.append([i, j])
                    while(q):
                        cur = q.pop(0)
                        cur_i = cur[0]
                        cur_j = cur[1]

                        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                        for k in direction:
                            next_i = cur_i + k[0]
                            next_j = cur_j + k[1]
                            if next_i < 0 or next_j < 0 or next_i >= len(grid) or next_j >= len(grid[0]):
                                continue 

                            if grid[next_i][next_j] == '1' and map[next_i][next_j] == 0:
                                q.append([next_i, next_j])
                                map[next_i][next_j] = 1
                else:
                    continue
        return ans
 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]

]

a = Solution()
print(a.numIslands(grid))