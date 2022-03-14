# 你现在手里有一份大小为 n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地。

# 请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。如果网格上只有陆地或者海洋，请返回 -1。

# 我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = []
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i, j])

        if not q:
            return -1
        if len(q) == len(grid[0]) * len(grid):
            return -1

        depth = 0
        while(q):
            size = len(q)

            for k in range(size):
                cur = q.pop(0)

                for d in directions:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and visit[x][y] == 0:
                        visit[x][y] = 1
                        q.append([x, y])
            
            depth += 1
        
        return depth - 1



grid = [[0,0,1,1,1],[0,1,1,0,0],[0,0,1,1,0],[1,0,0,0,0],[1,1,0,0,1]]
a = Solution()
print(a.maxDistance(grid))
