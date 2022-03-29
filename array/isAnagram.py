# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = collections.Counter(s)
        s2 = collections.Counter(t)

        if len(s1) != len(s2):
            return False
        
        for key in s1:
            if s1[key] != s2[key]:
                return False
        
        return True

s = "anagram"
t = "nagaram"

a = Solution()
print(a.isAnagram(s, t))