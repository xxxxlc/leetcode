# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.backtrack(n, [], 0, k)
        return self.ans

    def backtrack(self, s, track, t, k):
        if s == 0:
            if len(track) == k:
                self.ans.append(track[:])
            return
        
        for i in range(t + 1, 10):
            self.backtrack(s - i, track + [i], i, k)




k = 3
n = 9

a = Solution()
print(a.combinationSum3(k, n))
