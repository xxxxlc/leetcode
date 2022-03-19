# n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

# 路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。

# 今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

# 请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

# 题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        conc = [[] for _ in range(n)]
        ucon = [[] for _ in range(n)]
        for i in range(len(connections)):
            conc[connections[i][0]].append(connections[i][1])
            ucon[connections[i][0]].append(connections[i][1])
            ucon[connections[i][1]].append(connections[i][0])

        visited = [0 for _ in range(n)]
        visited[0] = 1
        ans = 0
        q = [0]
        while(q):
            size = len(q)

            for k in range(size):
                cur = q.pop(0)

                for node in ucon[cur]:
                    if visited[node] == 0:
                        if node not in conc[cur]:
                            ans += 1
                        q.append(node)
                        visited[node] = 1
        
        return n - 1 - ans
                    


n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

a = Solution()
print(a.minReorder(n, connections))