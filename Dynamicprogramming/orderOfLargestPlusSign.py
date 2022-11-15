# 在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示 grid[xi][yi] == 0

# 返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。

# 一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。


class Solution(object):

    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        dp = [[n] * n for _ in range(n)]
        banned = set(map(tuple, mines))
        for i in range(n):
            # left
            count = 0
            for j in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # right
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        for j in range(n):
            # up
            count = 0
            for i in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # down
            count = 0
            for i in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        return max(map(max, dp))

            

    # 暴力做法
    # def orderOfLargestPlusSign(self, n, mines):
    #     """
    #     :type n: int
    #     :type mines: List[List[int]]
    #     :rtype: int
    #     """
    #     kmax = 0
    #     grid = [[1 for _ in range(n)] for _ in range(n)]
    #     direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    #     for i, j in mines:
    #         grid[i][j] = 0

    #     for i in range(0, n):
    #         for j in range(0, n):
    #             if grid[i][j] == 0:
    #                 continue
    #             for k in range(1, n):
    #                 havePlusSign = True
    #                 for d in direction:
    #                     if i + d[0] * k < 0 or i + d[0] * k >= n or j + d[1] * k < 0 or j + d[1] * k >= n:
    #                         havePlusSign = False
    #                         break
    #                     if grid[i + d[0] * k][j + d[1] * k] == 0:
    #                         havePlusSign = False
    #                         break
    #                 if not havePlusSign:
    #                     break
                

    #             kmax = max(k, kmax)
    #     return kmax

                    



n = 2
mines = [[0,0],[0,1],[1,0]]

a = Solution()
print(a.orderOfLargestPlusSign(n, mines))