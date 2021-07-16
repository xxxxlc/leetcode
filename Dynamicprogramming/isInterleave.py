# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 提示：a + b 意味着字符串 a 和 b 连接。


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        

        dp = [[False for i in range(0, len(s2)+1)] for j in range(0, len(s1)+1)]

        dp[0][0] = True
        
        for i in range(0, len(s1)+1):
            for j in range(0, len(s2)+1):
                p = i + j - 1
                if i > 0:
                    dp[i][j] = (dp[i-1][j] and s3[p] == s1[i-1]) or dp[i][j]
                if j > 0:
                    dp[i][j] = (dp[i][j-1] and s3[p] == s2[j-1]) or dp[i][j]
        
        return dp[len(s1)][len(s2)]



s1 = "aa"
s2 = "ab"
s3 = 'abaa'
a = Solution()
print(a.isInterleave(s1, s2, s3))