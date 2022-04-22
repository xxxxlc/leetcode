# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        stack = [""] * numRows

        if numRows == 1:
            return s

        i = 0

        while (i < len(s)):
            if i == 0:
                stack[0] += s[i]
                i += 1
            
            for j in range(1, numRows):
                if i < len(s):
                    stack[j] += s[i]
                    i += 1
            
            for j in range(numRows - 2, -1, -1):
                if i < len(s):
                    stack[j] += s[i]
                    i += 1
        ans = ""
        for i in range(0, numRows):
            ans += stack[i]

        return ans


s = "AB"
numRows = 1

a = Solution()
print(a.convert(s, numRows))