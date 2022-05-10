# 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。

# 在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。

import collections

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)

        single = 0
        ans = 0

        for key, value in c.items():
            if value % 2 == 0:
                ans += value
            else:
                single = 1
                ans += value - 1
        
        return ans + single



s = "abccccdd"

a = Solution()
print(a.longestPalindrome(s))