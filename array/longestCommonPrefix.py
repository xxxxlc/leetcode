# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        length = float('inf')
        for i in range(len(strs)):
            if len(strs[i]) < length:
                length = len(strs[i])

        same = True
        for i in range(length):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    same = False
            if same:
                ans += ch
            else:
                break

        return ans

strs = ["flower","flow","flight"]
a = Solution()
print(a.longestCommonPrefix(strs))