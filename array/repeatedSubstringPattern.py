# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                c = s[:i]
                isTrue = True
                for j in range(1, int(len(s) / i)):
                    if c != s[i*j:i*(j+1)]:
                        isTrue = False
                        break
                if isTrue:
                    return True
        return False

s = "a"

a = Solution()
print(a.repeatedSubstringPattern(s))