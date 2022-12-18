# 给你一个有 n 个节点的 无向 图，节点编号为 1 到 n 。再给你整数 n 和一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条边。图不一定连通。

# 你可以给图中添加 至多 两条额外的边（也可以一条边都不添加），使得图中没有重边也没有自环。

# 如果添加额外的边后，可以使得图中所有点的度数都是偶数，返回 true ，否则返回 false 。

# 点的度数是连接一个点的边的数目。

from collections import Counter, defaultdict

class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        grid = defaultdict(set)
        deg = Counter()


        for x, y in edges:
            
            grid[x].add(y)
            grid[y].add(x)

            deg[x] += 1
            deg[y] += 1
        
        odd = [i for i, d in deg.items() if d % 2]
        m = len(odd)

        if m == 0:
            return True
        
        if m == 2:
            x, y, = odd
            if x not in grid[y]:
                return True
            
            for i in range(1, n + 1):
                if i != x and i != y and x not in grid[i] and y not in grid[i]:
                    return True
            return False
        
        if m == 4:
            a, b, c, d = odd
            return b not in grid[a] and c not in grid[d] or \
                   c not in grid[a] and d not in grid[b] or \
                   d not in grid[a] and c not in grid[b] 
            
        return False

        




n = 5
edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]

a = Solution()
print(a.isPossible(n, edges))