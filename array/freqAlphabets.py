# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：

# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
# 返回映射之后形成的新字符串。

# 题目数据保证映射始终唯一。


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = len(s) - 1
        ans = ""
        while (i >= 0):
            if s[i] == "#":
                c = chr(int(s[i-2:i]) + ord('a') - 1)
                ans = c + ans
                i -= 3
            else:
                c = chr(ord('a') + int(s[i]) - 1)
                ans = c + ans
                i -= 1
        return ans


s = "10#11#12"

a = Solution()
print(a.freqAlphabets(s))