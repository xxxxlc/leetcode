# 句子 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。

# 例如，"Hello World"、"HELLO" 和 "hello world hello world" 都是句子。
# 给你一个句子 s​​​​​​ 和一个整数 k​​​​​​ ，请你将 s​​ 截断 ​，​​​使截断后的句子仅含 前 k​​​​​​ 个单词。返回 截断 s​​​​​​ 后得到的句子。

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(0, len(s)):
            if s[i] == ' ':
                k = k - 1
                if k == 0:
                    return s[0:i]
        return s



s = "Hello how are you Contestant"
k = 4

a = Solution()
print(a.truncateSentence(s, k))