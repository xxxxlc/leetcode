# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

# 如果可以，返回 true ；否则返回 false 。

# magazine 中的每个字符只能在 ransomNote 中使用一次。


import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        charmap = collections.Counter(magazine)
        
        for c in ransomNote:
            if charmap.get(c, 0) == 0:
                return False
            charmap[c] = charmap[c] - 1

        return True 

ransomNote = "aa"
magazine = "ab"

a = Solution()
print(a.canConstruct(ransomNote, magazine))
