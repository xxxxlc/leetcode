# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。




class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = dict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p): 
                return i == len(s)

            first = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p) - 2 and p[j + 1] == '*':
                ans =  dp(i, j + 2) or (first and dp(i + 1, j))
            else:
                ans =  first and dp(i + 1, j + 1)
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)




a = Solution()
s = "aa"
p = "a*"
print(a.isMatch(s, p))