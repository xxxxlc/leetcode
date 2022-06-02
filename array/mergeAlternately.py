# 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0

        m = len(word1)
        n = len(word2)
        ans = ""

        while (i < m and j < n):
            ans += word1[i]
            i += 1
            ans += word2[j]
            j += 1
        
        ans += word2[j:n] if i == m else word1[i:m]
        return ans

word1 = "abjkghd"
word2 = "pqrs"

a = Solution()
print(a.mergeAlternately(word1, word2))