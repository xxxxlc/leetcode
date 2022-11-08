# 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。

# 请你返回 words 数组中 一致字符串 的数目。

from collections import Counter

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for word in words:
            isAllowed = True
            for c in word:
                if c not in allowed: 
                    isAllowed = False
                    break
            if isAllowed:
                ans += 1
        return ans

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

a = Solution()
print(a.countConsistentStrings(allowed, words))
