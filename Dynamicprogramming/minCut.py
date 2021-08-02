# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

# 返回符合要求的 最少分割次数 



class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])

        f = [float('inf')] * n
        for i in range(0, n):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(0, i):
                    if dp[j+1][i]:
                        f[i] = min(f[i], f[j] + 1)

        return f[n - 1]


s = "leet"

a = Solution()
print(a.minCut(s))