# 给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。

# 每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 entrance 最近 的出口。出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。

# 请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。




class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        exit = []
        m = len(maze)
        n = len(maze[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[0 for _ in range(n)] for _ in range(m)]


        for i in range(m):
            if maze[i][0] == ".":
                exit.append([i, 0])
            if maze[i][n - 1] == ".":
                exit.append([i ,n - 1])
        
        for i in range(1, n - 1):
            if maze[0][i] == ".":
                exit.append([0, i])
            if maze[m - 1][i] == ".":
                exit.append([m - 1, i])
        
        if entrance in exit:
            exit.remove(entrance)
        q = []
        q.append(entrance)
        visited[entrance[0]][entrance[1]] = 1

        ans = 0
        isfind = False
        while(q):
            size = len(q)

            for k in range(size):
                cur = q.pop(0)

                for d in direction:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < m and 0 <= y < n and visited[x][y] == 0 and maze[x][y] == ".":
                        if [x, y] in exit:
                            isfind = True
                        q.append([x, y])
                        visited[x][y] = 1
            ans += 1
            if isfind:
                return ans
        
        return -1


maze =  [[".","+"]]
entrance = [0, 0]

a = Solution()
print(a.nearestExit(maze, entrance))