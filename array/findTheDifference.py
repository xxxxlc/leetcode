# 给定两个字符串 s 和 t ，它们只包含小写字母。

# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

# 请找出在 t 中被添加的字母。

import collections

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = collections.Counter(s)
        t = collections.Counter(t)
        
        for key in t.keys():
            if key not in s:
                return key
            if t[key] != s[key]:
                return key 

s = "abcd"
t = "abcde"

a = Solution()
print(a.findTheDifference(s, t))