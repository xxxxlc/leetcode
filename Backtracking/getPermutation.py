# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.ans = []
        self.backtrack(n, k, [])
        return "".join([str(i) for i in self.ans[-1]])

    def backtrack(self, n, k, track):
        if len(self.ans) == k:
            return
        if len(track) == n:
            self.ans.append(track[:])
            return
        
        for i in range(1, n + 1):
            if i not in track:
                self.backtrack(n, k, track + [i])
    
    def solution_math(self, n, k):
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)


n = 3
k = 1

a = Solution()
print(a.getPermutation(n, k))