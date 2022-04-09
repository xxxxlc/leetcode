# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。

# 每步 可以删除任意一个字符串中的一个字符。


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return m + n - 2 * dp[m][n]


word1 = "sea"
word2 = "eat"

a = Solution()
print(a.minDistance(word1, word2))