# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

# 返回矩阵中 省份 的数量。



class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        ans = 0
        visited = [0 for _ in range(len(isConnected))]

        for i in range(len(isConnected)):
            if visited[i] == 0:
                ans += 1
                q = [i]
                while(q):
                    size = len(q)

                    for k in range(size):
                        cur = q.pop(0)

                        for m in range(0, len(isConnected)):
                            if isConnected[cur][m] == 1 and visited[m] == 0:
                                q.append(m)
                                visited[m] = 1
        
        return ans


isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
a = Solution()
print(a.findCircleNum(isConnected))
