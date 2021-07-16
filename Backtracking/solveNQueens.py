# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        board = [[0]*n for i in range (0, n)]
        # print(board)
        self.backtrack(board, 0)
        res = self.num2str()
        return res
    
    def backtrack(self, board, row):
        if row == len(board):
            temp = [board[i][:] for i in range(0, len(board))]
            self.res.append(temp)
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

    def num2str(self):
        res = []
        for k in range(0, len(self.res)):
            temp1 = []
            for i in range(0, len(self.res[0])):
                temp = ""
                for j in range(0, len(self.res[0][0])):
                    if self.res[k][i][j] == 1:
                        temp += "Q"
                    else:
                        temp += "."
                temp1.append(temp)
            res.append(temp1)
        return res





a = Solution()
print(a.solveNQueens(4))