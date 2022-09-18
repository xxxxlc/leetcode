# 字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。

# 例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
# 给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。


class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        maxLength = 1
        length = 1
        for i in range(1, len(s)):
            if s[i] == chr(ord(s[i - 1]) + 1):
                length += 1
                maxLength = max(maxLength, length)
            else:
                length = 1
        
        return maxLength

s = "abcdefghijklmnopqrstuvwxyz"

a = Solution()
print(a.longestContinuousSubstring(s))