# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

# 两个相邻元素间的距离为 1 。

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dis = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        visited = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = []
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 0:
                    q.append([i, j])
                    visited[i][j] = 1
        
        distance = 0
        while(q):
            distance += 1

            for k in range(len(q)):
                cur = q.pop(0)

                for d in directions:
                    x = cur[0] + d[0]
                    y = cur[1] + d[1]

                    if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and visited[x][y] == 0:
                        q.append([x, y])
                        dis[x][y] = distance
                        visited[x][y] = 1
        
        return dis

                
mat = [[0,0,0],[0,1,0],[1,1,1]]

a = Solution()
print(a.updateMatrix(mat))