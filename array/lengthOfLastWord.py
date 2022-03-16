# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while(s[i] == " "):
            i = i - 1
        j = i
        while(i >= 0 and s[i] != " "):
            i = i - 1
        
        return j - i


s = "a"
a = Solution()
print(a.lengthOfLastWord(s))
