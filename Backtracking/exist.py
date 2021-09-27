# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        # vector = [[0,1],[0,-1],[-1,0],[1,0]]

        for row in range(0, m):
            for col in range(0, n):
                if board[row][col] == word[0]:
                    q = []
                    q.append([row, col])
                else:
                    continue
                mp = [[0 for _ in range(n)] for _ in range(m)]
                mp[row][col] = 1
                if self.trackback(word, board, mp, row, col, 1):
                    return True

                # while(q):
                #     if k == len(word):
                #         return True
                #     size = len(q)
                #     for i in range(0, size):
                #         cur = q.pop(0)

                #         for v in vector:
                #             if 0 <= cur[0] + v[0] < m and 0 <= cur[1] + v[1] < n:
                #                 if board[cur[0] + v[0]][cur[1] + v[1]] == word[k]:
                #                     q.append([cur[0] + v[0], cur[1] + v[1]])
                #                     mp[cur[0] + v[0]][cur[1] + v[1]] = 1
                        
                #     k = k + 1
                
        
        return False

    def trackback(self, word, board, mp, row, col, k):
        vector = [[0,1],[0,-1],[-1,0],[1,0]]
        if k == len(word):
            return True
        
        for v in vector:
            if 0 <= row + v[0] < len(mp) and 0 <= col + v[1] < len(mp[0]):
                if mp[row + v[0]][col + v[1]] ==0 and board[row + v[0]][col + v[1]] == word[k]:
                    mp[row + v[0]][col + v[1]] = 1
                    if self.trackback(word, board, mp, row + v[0], col + v[1], k + 1):
                        return True
                    mp[row + v[0]][col + v[1]] = 0





board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
a = Solution()

print(a.exist(board, word))

