# 在本问题中, 树指的是一个连通且无环的无向图。

# 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

# 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

# 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

import UF

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []
        uf = UF.UF(len(edges)+1)

        for i in range(0, len(edges)):
            if uf.connected(edges[i][0], edges[i][1]) == True:
                return edges[i]
            else:
                uf.union(edges[i][0], edges[i][1])
        


edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]

a = Solution()
print(a.findRedundantConnection(edges))