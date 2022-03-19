# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1

        while(i <= j):
            if not (s[i].isdigit() or s[i].isalpha()):
                i = i + 1
                continue
            if not (s[j].isdigit() or s[j].isalpha()):
                j = j - 1
                continue
            
            if s[i].isdigit():
                if s[i] != s[j]:
                    return False
                else:
                    i = i + 1
                    j = j - 1
                    continue

            if s[i].isalpha():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i = i + 1
                    j = j - 1

        return True


s = "0z;z   ; 0"
a = Solution()
print(a.isPalindrome(s))