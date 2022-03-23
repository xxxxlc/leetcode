# 给你一个 有向无环图 ， n 个节点编号为 0 到 n-1 ，以及一个边数组 edges ，其中 edges[i] = [fromi, toi] 表示一条从点  fromi 到点 toi 的有向边。

# 找到最小的点集使得从这些点出发能到达图中所有点。题目保证解存在且唯一。

# 你可以以任意顺序返回这些节点编号。


class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        endSet = set(y for x, y in edges)
        ans = [i for i in range(n) if i not in endSet]
        return ans



n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

a = Solution()
print(a.findSmallestSetOfVertices(n, edges))