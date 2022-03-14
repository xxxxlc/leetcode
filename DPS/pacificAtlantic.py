# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。

# 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。

# 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

# 返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋 。




class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.m = len(heights)
        self.n = len(heights[0])

        po = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        ao = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]

        for i in range(0, self.n):
            self.dfs(heights, 0, i, po)
            self.dfs(heights, self.m - 1, i, ao)
        for i in range(0, self.m):
            self.dfs(heights, i, 0, po)
            self.dfs(heights, i, self.n - 1, ao)

        for i in range(0, self.m):
            for j in range(0, self.n):
                if po[i][j] == 1 and ao[i][j] == 1:
                    ans.append([i, j])
        return ans

    def dfs(self, heights, x, y, tmp):
        tmp[x][y] = 1

        for d in self.directions:
            cur_x = x + d[0]
            cur_y = y + d[1]

            if (not self.in_area(cur_x, cur_y) or heights[x][y] > heights[cur_x][cur_y] or tmp[cur_x][cur_y] == 1):
                continue

            self.dfs(heights, cur_x, cur_y, tmp)
 
    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n
    

        


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

a = Solution()
print(a.pacificAtlantic(heights))