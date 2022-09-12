# 给你一个字符串 s ，请你将该字符串划分成一个或多个 子字符串 ，并满足每个子字符串中的字符都是 唯一 的。也就是说，在单个子字符串中，字母的出现次数都不超过 一次 。

# 满足题目要求的情况下，返回 最少 需要划分多少个子字符串。

# 注意，划分后，原字符串中的每个字符都应该恰好属于一个子字符串。


class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """

        j = 0
        window = set()
        divideNum = 0

        while(j < len(s)):
            if s[j] not in window:
                window.add(s[j])
                j += 1
            else:
                divideNum += 1
                window = set()
        
        return divideNum + 1


s = "ssssss"

a = Solution()
print(a.partitionString(s))