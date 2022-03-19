# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。

# red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

# 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。




from platform import node

from matplotlib.pyplot import flag


class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        rededges = [[] for _ in range(n)]
        blueedges = [[] for _ in range(n)]
        ans = [float('inf')] * n

        for i in range(len(redEdges)):
            rededges[redEdges[i][0]].append(redEdges[i][1])

        for i in range(len(blueEdges)):
            blueedges[blueEdges[i][0]].append(blueEdges[i][1])

        q = [(0, True, 0), (0, False, 0)]

        bv = [False] * n
        rv = [False] * n

        while q:
            node, flag, step = q.pop(0)
            ans[node] = min(ans[node], step)

            if flag:
                v = bv
            else:
                v = rv
            v[node] = True
            g = rededges if flag else blueedges
            v = rv if flag else bv

            for node in g[node]:
                if v[node]:
                    continue
                q.append((node, not flag, step + 1))
        
        ans = [x if x != float('inf') else -1 for x in ans]
        return ans


        
         




n = 5
red_edges = [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
blue_edges = [[1,3],[0,0],[0,3],[4,2],[1,0]]

a = Solution()
print(a.shortestAlternatingPaths(n, red_edges, blue_edges))