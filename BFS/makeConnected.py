# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

# 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        m = len(connections)
        if m < n - 1:
            return -1

        visited = [0 for _ in range(n)]

        isconnect = [[] for _ in range(n)]

        for i in range(len(connections)):
            isconnect[connections[i][0]].append(connections[i][1])
            isconnect[connections[i][1]].append(connections[i][0])

        ans = 0

        for i in range(n):
            if visited[i] == 0:
                ans += 1
                visited[i] = 1

                q = [i]

                while(q):
                    size = len(q)

                    for k in range(size):
                        cur = q.pop(0)
                        for com in isconnect[cur]:
                            if visited[com] == 0:
                                q.append(com)
                                visited[com] = 1

        return ans - 1

        

        


n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

a = Solution()
print(a.makeConnected(n ,connections))