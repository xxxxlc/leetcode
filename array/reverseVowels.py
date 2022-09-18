# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        i = 0
        j = len(s) - 1

        while(i < j):
            while(i < len(s) and s[i] not in Vowels):
                i += 1
            
            while(j >= 0 and s[j] not in Vowels):
                j -= 1
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return ''.join(s)

s = ",."
a = Solution()
print(a.reverseVowels(s))