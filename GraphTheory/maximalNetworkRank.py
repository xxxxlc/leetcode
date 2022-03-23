# n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有一条双向道路。

# 两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。

# 整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。

# 给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        edges = [[] for _ in range(n)]

        for i in range(len(roads)):
            edges[roads[i][0]].append(roads[i][1])
            edges[roads[i][1]].append(roads[i][0])
        
        max_len = 0
        for i in range(n):
            for j in range(i + 1, n):
                t_len = len(edges[i]) + len(edges[j])

                if i in edges[j]:
                    t_len -= 1
                
                if t_len > max_len:
                    max_len = t_len
        return max_len

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]

a = Solution()
print(a.maximalNetworkRank(n, roads))