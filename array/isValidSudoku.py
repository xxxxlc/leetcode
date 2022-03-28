# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
#  

# 注意：

# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用 '.' 表示。

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.append(board[j][i])
        
        for i in range(3):
            for j in range(3):
                p = []
                for m in range(3):
                    for n in range(3):
                        if board[3 * i + m][3 * j + n] != ".":
                            if board[3 * i + m][3 * j + n] in p:
                                return False
                            p.append(board[3 * i + m][3 * j + n])
        
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

a = Solution()
print(a.isValidSudoku(board))