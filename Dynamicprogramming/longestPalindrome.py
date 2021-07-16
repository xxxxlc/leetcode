# 给你一个字符串 s，找到 s 中最长的回文子串


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        dp = [[False for i in range(len(s))] for j in range(len(s))]

        for i in range(0, len(s)):
            dp[i][i] = True

        maxlength = 0
        begin = 0
        for j in range(1, len(s)):
            for i in range(0, j):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and j - i > maxlength:
                    maxlength = j - i
                    begin = i

        return s[begin:begin + maxlength + 1]
        
        



s = 'babab'
a = Solution()
print(a.longestPalindrome(s))