# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。

# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。

# 例如， “ace” 是 “abcde” 的子序列。

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for word in words:
            if self.issubseq(word, s, 0):
                ans += 1
                # print(word)
        
        
        return ans

    def issubseq(self, s1, s2, idx):
        if len(s1) == 0:
            return True
        if len(s2) == 0:
            return False

        i = s2.find(s1[0], idx)
        if i == -1:
            return False
        else:
            return self.issubseq(s1[1:], s2, i + 1)


s = "abcde"
words = ["a","bb","acd","ace"]

a = Solution()
print(a.numMatchingSubseq(s, words))