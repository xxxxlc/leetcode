# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        left = 0
        for i in range(len(s)):
            if s[i] == ' ':
                ans += ''.join(reversed(s[left:i]))
                ans += ' '
                left = i + 1
            elif i == len(s) - 1:
                ans += ''.join(reversed(s[left:i + 1]))
        
        return ans


s = "Let's take LeetCode contest"
a = Solution()
print(a.reverseWords(s))