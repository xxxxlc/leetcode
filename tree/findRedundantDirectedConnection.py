# 在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。

# 输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。

# 结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。

# 返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

class Unionfind(object):
    def __init__(self, n):
        self.parent = []
        for i in range(0, n):
            self.parent.append(i)
    
    def find(self, x):
        while(self.parent[x] != x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        rootQ = self.find(q)
        rootP = self.find(p)

        if rootP == rootQ:
            return
        
        self.parent[rootP] = rootQ
    
    def connected(self, p, q):
        rootQ = self.find(q)
        rootP = self.find(p)

        return rootP == rootQ

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []
        uf = Unionfind(len(edges) + 1)
        parent = list(range(len(edges)+1))
        conflict = -1
        cycle = -1
        for i in range(0, len(edges)):
            if parent[edges[i][1]] != edges[i][1]:
                conflict = i
            else:
                parent[edges[i][1]] = edges[i][0]
                if uf.connected(edges[i][0], edges[i][1]):
                    cycle = i
                else:
                    uf.union(edges[i][0], edges[i][1])
        
        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]
        



edges = [[1,2],[1,3],[2,3]]

a = Solution()
print(a.findRedundantDirectedConnection(edges))