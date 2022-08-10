# 根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]

        for row in range(m):
            for col in range(n):
                liveCell = 0
                for d in neighbors:
                    x = row + d[0]
                    y = col + d[1]
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                        liveCell += 1
                if liveCell < 2:
                    ans[row][col] = 0
                elif 2<= liveCell <= 3:
                    if board[row][col] == 1:
                        ans[row][col] = 1
                    if board[row][col] == 0 and liveCell == 3:
                        ans[row][col] = 1
                else:
                    ans[row][col] = 0
        for row in range(m):
            for col in range(n):
                board[row][col] = ans[row][col]
        

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

a = Solution()
print(a.gameOfLife(board))