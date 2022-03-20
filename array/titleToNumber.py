# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0

        for i in range(len(columnTitle)):
            ans *= 26
            ans += ord(columnTitle[i]) - 64
        
        return ans


columnTitle = "ZY"

a = Solution()
print(a.titleToNumber(columnTitle))