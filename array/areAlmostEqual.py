# 给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

# 如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        n = len(s1)
        m = [i for i in range(n) if s1[i] != s2[i]]
        if len(m) != 2:
            return False
        if s1[m[0]] == s2[m[1]] and s1[m[1]] == s2[m[0]]:
            return True
        return False
        



s1 = "bank"
s2 = "kanb"

a = Solution()
print(a.areAlmostEqual(s1, s2))
