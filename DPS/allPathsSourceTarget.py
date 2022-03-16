# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

#  graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。

from matplotlib.pyplot import table


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.path = []

        self.dfs(graph, [0])

        return self.path
        
    
    def dfs(self, graph, track):
        if track[-1] == len(graph) - 1:
            self.path.append(track[:])
            return
        nodes = graph[track[-1]]
        for node in nodes:
            self.dfs(graph, track + [node])




graph = [[1,2],[3],[3],[]]
a = Solution()
print(a.allPathsSourceTarget(graph))
