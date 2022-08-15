# 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                isSame = False
                for m in words[i]:
                    for n in words[j]:
                        if m == n:
                            isSame = True
                if not isSame:
                    ans = max(ans, len(words[i] * len(words[j])))
        
        return ans


words = ["abcw","baz","foo","bar","xtfn","abcdef"]

a = Solution()
print(a.maxProduct(words))

