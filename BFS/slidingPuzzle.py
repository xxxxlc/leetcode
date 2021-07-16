# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.

# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.

# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        target = '123450'
        start = ''
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                start += str(board[i][j])
        
        neighbor = [
            [1,3],
            [0,2,4],
            [1,5],
            [0,4],
            [1,3,5],
            [2,4]
        ]

        visited = set()
        q = []
        q.append(start)
        step = 0
        while(q):
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)

                if cur == target:
                    return step

                idx = cur.index('0')
                for j in neighbor[idx]:
                    if idx < j:
                        new_board = cur[:idx] + cur[j] + cur[idx+1:j] + cur[idx] + cur[j+1:]
                    else:
                        new_board = cur[:j] + cur[idx] + cur[j+1:idx] + cur[j] + cur[idx+1:]
                    # print(new_board)
                    if new_board not in visited:
                        q.append(new_board)
                        visited.add(new_board)

            step += 1
        return -1



a = Solution()
board = [[4,1,2],[5,0,3]]
print(a.slidingPuzzle(board))