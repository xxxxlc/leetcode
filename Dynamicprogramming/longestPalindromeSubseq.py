# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。



class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        t = s[::-1]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n][n]


s = "bbbbab"

a = Solution()
print(a.longestPalindromeSubseq(s))