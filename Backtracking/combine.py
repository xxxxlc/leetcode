# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        track = []
        self.backtrack(n, k, 1, track)
        return self.res

    def backtrack(self, n, k, start, track):
        if k == len(track):
            self.res.append(track[:])
            return 
        
        for i in range(start, n + 1):
            track.append(i)
            self.backtrack(n, k, i + 1, track)
            track.pop(-1)

n = 4
k = 2
a = Solution()
print(a.combine(n, k))
