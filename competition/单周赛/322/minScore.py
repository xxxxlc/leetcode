# 给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。给你一个二维数组 roads ，其中 roads[i] = [ai, bi, distancei] 表示城市 ai 和 bi 之间有一条 双向 道路，道路距离为 distancei 。城市构成的图不一定是连通的。

# 两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。

# 城市 1 和城市 n 之间的所有路径的 最小 分数。


# 注意：

# 一条路径指的是两个城市之间的道路序列。
# 一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。
# 测试数据保证城市 1 和城市n 之间 至少 有一条路径

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        grid = [[] for _ in range(n)]

        for x, y, d in roads:
            x -= 1
            y -= 1

            grid[x].append((y, d))
            grid[y].append((x, d))

        ans = float('inf')
        visited = [False] * n
        def dfs(x: int) -> None:
            nonlocal ans
            visited[x] = True

            for y, d in grid[x]:
                ans = min(ans, d)
                if not visited[y]:
                    dfs(y)
        
        dfs(0)

        return ans




n = 14
roads =    [[2,9,2308],[2,5,2150],[12,3,4944],[13,5,5462],[2,10,2187],[2,12,8132],[2,13,3666],[4,14,3019],[2,4,6759],[2,14,9869],[1,10,8147],[3,4,7971],[9,13,8026],[5,12,9982],[10,9,6459]]

a = Solution()
print(a.minScore(n, roads))