# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        board = [[0]*n for i in range (0, n)]
        self.backtrack(board, 0)
        return self.ans
    
    def backtrack(self, board, row):
        if row == len(board):
            self.ans += 1
            return
        for col in range(0, len(board)):

            if not self.isVaild(board, row, col):
                continue

            board[row][col] = 1
            self.backtrack(board, row + 1)
            board[row][col] = 0
    
    def isVaild(self, board, row, col):
        n = len(board)

        for i in range(0, n):
            if board[i][col] == 1:
                return False
        i = row - 1
        j = col - 1
        while(i >= 0 and j >= 0):
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        i = row - 1
        j = col + 1
        while(i >= 0 and j < n):
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        
        return True






a = Solution()
print(a.totalNQueens(4))
