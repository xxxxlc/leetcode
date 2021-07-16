# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
import UF

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        
        m = len(board)
        n = len(board[0])

        uf = UF.UF(m * n + 1)

        dummy = m * n 
        for i in range(0, m):
            if board[i][0] == 'O':
                uf.union(i * n, dummy)
            
            if board[i][n - 1] == 'O':
                uf.union(i * n + n - 1, dummy)

        for i in range(0, n):
            if board[0][i] == 'O':
                uf.union(i, dummy)
            if board[m - 1][i] ==  'O':
                uf.union((m - 1) * n + i, dummy)
        
        d = [[1,0],[0,1],[0,-1],[-1,0]]
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for k in range(0, 4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            uf.union(x * n + y, i * n + j)
                            # print(x, y , uf.find(x * n + y), uf.find(i * n + y))
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = 'X'
        





board =[["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
a = Solution()
a.solve(board)
print(board)