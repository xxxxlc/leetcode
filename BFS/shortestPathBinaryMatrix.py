# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        visted = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        if grid[0][0] == 1:
            return -1
        ans = None
        depth = 1
        q = [[0, 0]]
        visted[0][0] = 1

        while(q):
            size = len(q)

            for k in range(size):
                cur = q.pop(0)

                if cur[0] == len(grid) - 1 and cur[1] == len(grid[0]) - 1:
                    ans = depth

                for d in direction:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visted[x][y] == 0 and grid[x][y] == 0:
                        q.append([x, y])
                        visted[x][y] = 1
            depth += 1
        
        if ans:
            return ans
        return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]

a = Solution()
print(a.shortestPathBinaryMatrix(grid))
