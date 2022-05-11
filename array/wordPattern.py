# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。

# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

import collections

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        x = dict()
        s = s.split(" ")

        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in x:
                if s[i] not in x.values():
                    x[pattern[i]] = s[i]
                else:
                    return False
            else:
                if s[i] != x[pattern[i]]:
                    return False
        
        return True
        

pattern = "abba"
str = "dog dog dog dog"

a = Solution()
print(a.wordPattern(pattern, str))
