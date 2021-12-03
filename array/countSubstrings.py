# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        ans = 0

        for i in range(0, len(s)):
            for j in range(0, 2):
                l = i
                r = i + j
                while(l>=0 and r < len(s)):
                    if s[l] == s[r]:
                        ans += 1
                        l = l - 1
                        r = r + 1
                    else:
                        break
        
        return ans
    



s = "abc"
a = Solution()
print(a.countSubstrings(s))