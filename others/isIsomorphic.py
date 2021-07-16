# 给定两个字符串 s 和 t，判断它们是否是同构的。

# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)) or len(s) != len(t):
            return False
        char_dict = {}
        for index in range(len(s)):
            if char_dict.get(s[index], 0) == 0:
                char_dict[s[index]] = t[index]
            elif char_dict.get(s[index], 0) != t[index]:
                return False
        return True
            


a = Solution()
s = 'egg'
t = 'add'
print(a.isIsomorphic(s, t))
