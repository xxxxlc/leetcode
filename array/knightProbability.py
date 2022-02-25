# 在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。

# 象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        way = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, -1], [2, 1], [-2, 1], [-2, -1]]
        ans = 1
        locations = [[row, column]]
        
        while(locations):
            if k == 0:
                break
            loc = 0
            allpro = len(locations) * len(way)
            for i in range(0, len(locations)):
                cur = locations.pop(0)

                for s in way:
                    row = cur[0] + s[0]
                    col = cur[1] + s[1]

                    if row < 0 or col < 0 or row > n - 1 or col > n - 1:
                        continue

                    locations.append([row, col])
                    loc += 1
            
            ans = ans * loc / allpro

            k = k - 1 
        
        return ans
        


n = 3
k = 2
row = 0
column = 0

a = Solution()
print(a.knightProbability(n, k, row, column))