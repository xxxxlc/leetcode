# 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。

# 给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。

import collections


class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = {}
        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            for nxt in graph[node]:
                if not dfs(nxt, c^1):
                    return False
            return True
        
        for i in range(1, n+1):
            if i not in color:
                if not dfs(i):
                    return False
        return True
            

n = 4
dislikes = [[1,2],[1,3],[2,4]]

a = Solution()
print(a.possibleBipartition(n, dislikes))