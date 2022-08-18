# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。

# 给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。

# 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。

# 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。

# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。

from collections import deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 暴力解法，超出时间限制
        # neighbor = [[] for _ in range(n)]
        # for i in range(len(edges)):
        #     neighbor[edges[i][0]].append(edges[i][1])
        #     neighbor[edges[i][1]].append(edges[i][0])

        # minHeight = float('inf')
        # minHeightNode = []

        # for node in range(n):
        #     visited = set()
        #     height = 0
        #     q = [node]
        #     visited.add(node)

        #     while(q):
        #         size = len(q)
        #         for _ in range(size):
        #             curNode = q.pop(0)

        #             for neighborNode in neighbor[curNode]:
        #                 if neighborNode not in visited:
        #                     visited.add(neighborNode)
        #                     q.append(neighborNode)
                
        #         height += 1
            
        #     if height < minHeight:
        #         minHeight = height
        #         minHeightNode = [node]
        #     elif height == minHeight:
        #         minHeightNode.append(node)

        # return minHeightNode


        # 找出最长路径的终点路径
        if n == 1:
            return [n]

        neighbor = [[] for _ in range(n)]
        for i in range(len(edges)):
            neighbor[edges[i][0]].append(edges[i][1])
            neighbor[edges[i][1]].append(edges[i][0])

        parents = [0] * n

        def bfs(start):
            visited = [False] * n
            visited[start] = True
            q = deque([start])

            while(q):
                x = q.popleft()
                for neighborNode in neighbor[x]:
                    if not visited[neighborNode]:
                        visited[neighborNode] = True
                        parents[neighborNode] = x
                        q.append(neighborNode)
            
            return x
        
        x = bfs(0)
        y = bfs(x)

        path = []
        parents[x] = -1
        while(y != -1):
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]
            

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

a = Solution()
print(a.findMinHeightTrees(n, edges))


