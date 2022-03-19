# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ""
        c = columnNumber % 26
        if c != 0:
            ans = chr(c + 64) + ans
        else:
            ans = "Z" + ans
        while(columnNumber > 26):
            columnNumber = (columnNumber - 1) // 26
            c = columnNumber % 26
            if c != 0:
                ans = chr(c + 64) + ans
            else:
                ans = "Z" + ans
        return ans


columnNumber = 2147483647

a = Solution()
print(a.convertToTitle(columnNumber))



