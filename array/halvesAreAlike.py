# 给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。

# 两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。

# 如果 a 和 b 相似，返回 true ；否则，返回 false 。

from collections import Counter

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = 0
        b = 0
        for i in range(len(s)):
            if s[i] in m:
                if i < len(s) // 2:
                    a += 1
                else:
                    b += 1
        
        return a == b
                 



s = "AbCdEfGh"

a = Solution()
print(a.halvesAreAlike(s))