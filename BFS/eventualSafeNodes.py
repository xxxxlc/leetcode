# 在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。

# 对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。

# 返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。

# 该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j) 是图的一条有向边。

class Solution(object):
    def eventualSafeNodes1(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        ans = set()

        for i in range(0, len(graph)):
            self.safenodes = []
            if i not in ans and self.dfs([i], graph, i):
                ans.add(i)
                for j in self.safenodes:
                    ans.add(j)
                
        ans = sorted(list(ans))
        return ans

    def dfs(self, path, graph, node):
        if not graph[node]:
            return True

        res = True
        for i in graph[node]:
            self.safenodes.append(i)
            if i in path:
                return False
            
            res = res and self.dfs(path + [i], graph, i)
        
        return res
    
    def eventualSafeNodes(self, graph):
        n = len(graph)
        color = [0] * n

        def safe(x: int) -> bool:
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x] = 2
            return True

        return [i for i in range(n) if safe(i)]

        

graph = [[1,2],[2,3],[5],[0],[5],[],[]]

a = Solution()
print(a.eventualSafeNodes(graph))