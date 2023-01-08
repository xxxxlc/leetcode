# 给你一个下标从 0 开始的 环形 字符串数组 words 和一个字符串 target 。环形数组 意味着数组首尾相连。

# 形式上， words[i] 的下一个元素是 words[(i + 1) % n] ，而 words[i] 的前一个元素是 words[(i - 1 + n) % n] ，其中 n 是 words 的长度。
# 从 startIndex 开始，你一次可以用 1 步移动到下一个或者前一个单词。

# 返回到达目标字符串 target 所需的最短距离。如果 words 中不存在字符串 target ，返回 -1 。


class Solution(object):
    def closetTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        idxs = []
        for i, word in enumerate(words):
            if word == target:
                idxs.append(i)
        
        if len(idxs) == 0:
            return -1
        
        mindistance = float('inf')

        for idx in idxs:
            if idx < startIndex:
                x = startIndex - idx
                y = idx + n - startIndex
            else:
                x = idx - startIndex
                y = startIndex + n - idx

            mindistance = min(min(mindistance, x), y)
        
        return mindistance


words = ["a","b","leetcode"]
target = "leetcode"
startIndex = 0


a = Solution()
print(a.closetTarget(words, target, startIndex))