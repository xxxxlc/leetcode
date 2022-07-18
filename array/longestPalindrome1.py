# 给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。

# 请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。

# 请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。

# 回文串 指的是从前往后和从后往前读一样的字符串。


class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = 0

        wordMap = {}

        for i in range(len(words)):
            wordMap[words[i]] = wordMap.get(words[i], 0) + 1
        
        wordSet = set()
        solo = False

        for key, value in wordMap.items():
            if key == key[::-1]:
                wordSet.add(key)
                length += wordMap[key] // 2 * 4
                if wordMap[key] % 2 != 0:
                    solo = True
                continue

            if key not in wordSet and key[::-1] in wordMap:
                wordSet.add(key)
                wordSet.add(key[::-1])
                length += min(wordMap[key], wordMap[key[::-1]]) * 4
        
        if solo:
            return length + 2
        else:
            return length

        

                


words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]

a = Solution()
print(a.longestPalindrome(words))