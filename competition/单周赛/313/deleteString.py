
# 给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以：

# 删除 整个字符串 s ，或者
# 对于满足 1 <= i <= s.length / 2 的任意 i ，如果 s 中的 前 i 个字母和接下来的 i 个字母 相等 ，删除 前 i 个字母。
# 例如，如果 s = "ababc" ，那么在一步操作中，你可以删除 s 的前两个字母得到 "abc" ，因为 s 的前两个字母和接下来的两个字母都等于 "ab" 。

# 返回删除 s 所需的最大操作数。\


class Solution(object):
    def deleteString1(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        if len(s) == 1:
            return 1
        self.ans = 0

        self.trackback(s, 1)
        return self.ans

    
    def trackback(self, s, num):
        if len(s) == 1:
            self.ans = max(self.ans, num)
            return
        
        i = 1
        isSplit = False
        while (i < len(s) // 2 + 1):
            for j in range(i + 1, len(s) + 1):
                if s[0:i] == s[i:j]:
                    self.trackback(s[i:], num + 1)
                    if not isSplit:
                        isSplit = True
            i += 1
        
        if not isSplit:
            self.ans = max(self.ans, num)
            return

    def deleteString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i], 1)
            for j in range(1, n - i + 1):
                if (i - j >= 0 and s[i:i+j] == s[i-j:i]):
                    dp[i - j] = max(dp[i - j], dp[i] + 1)
        
        return dp[0]





s = "aaaaa"

a = Solution()
print(a.deleteString(s))