# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）

# 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。

# 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）

from tracemalloc import start


class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        startx = None
        starty = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    startx = i
                    starty = j
                    break
            if not startx is None:
                break
        
        q = []
        q.append([startx, starty])
        visited[startx][starty] = 1

        island1 = [[startx, starty]]

        while(q):
            size = len(q)

            for k in range(size):
                cur = q.pop(0)

                for d in direction:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visited[x][y] == 0 and grid[x][y] == 1:
                        q.append([x, y])
                        island1.append([x, y])
                        visited[x][y] = 1
        
        depth = 0
        isfind = False
        while(island1):
            size = len(island1)

            for k in range(size):
                cur = island1.pop(0)

                for d in direction:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visited[x][y] == 0:
                        if grid[x][y] == 0:
                            island1.append([x, y])
                            visited[x][y] = 1
                        else:
                            isfind = True
            
            if isfind == True:
                return depth
            depth += 1




A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
a = Solution()
print(a.shortestBridge(A))