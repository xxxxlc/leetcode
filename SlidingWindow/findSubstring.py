# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。


import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        n = len(words[0])
        m = len(words)
        words = collections.Counter(words)
        ans = []

        for i in range(0, n):
            vaild = 0
            window = {}
            left = right = i

            while (right < len(s)):
                c = s[right:right + n]
                right += n

                if c not in words:
                    left = right
                    window.clear()
                    vaild = 0
                else:
                    vaild += 1
                    window[c] = window.get(c, 0) + 1

                    while (window[c] > words[c]):
                        d = s[left: left + n]
                        left += n
                        window[d] -= 1
                        vaild -= 1
                    
                    if vaild == m:
                        ans.append(left)
        return ans





        









s = "barfoothefoobarman"
words = ["foo","bar"]

a = Solution()
print(a.findSubstring(s, words))
