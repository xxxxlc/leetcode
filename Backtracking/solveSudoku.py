# 编写一个程序，通过填充空格来解决数独问题。

# 数独的解法需 遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)
    
    def backtrack(self, board, row, col):
        m = 9
        n = 9
        if col == m:
            return self.backtrack(board, row + 1, 0)
        
        if row == n:
            return True

        for i in range(row, m):
            for j in range(col, n):

                if board[i][j] != '.':
                    return self.backtrack(board, row, col + 1)
                
                for k in range(1, 10):
                    if not self.isVaild(board, i, j, k):
                        continue
                    board[i][j] = str(k)
                    if self.backtrack(board, i, j + 1):
                        return True
                    
                    board[i][j] = '.'
                return False
        return False

    def isVaild(self, board, row, col, k):
        for i in range(0, 9):
            if board[row][i] == str(k):
                return False
            if board[i][col] == str(k):
                return False
            
            if board[row//3 * 3 + i//3][col//3 * 3 + i%3] == str(k):
                return False
        
        return True
        
        
