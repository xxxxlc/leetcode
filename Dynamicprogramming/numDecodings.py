# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 



class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        else:
            return 0

        for i in range(2, len(s) + 1):
            if s[i-1] != '0':
                if int(s[i-2:i]) < 27 and s[i-2] !='0':
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if s[i-2] == '0':
                    return 0
                if int(s[i-2:i]) < 27:
                    dp[i] = dp[i-2]
                else:
                    return 0
        
        return dp[len(s)]


s = "16510056151031054105632484"
a = Solution()
print(a.numDecodings(s))