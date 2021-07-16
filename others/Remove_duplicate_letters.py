# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

import collections

class Solution(object):
    def __init__(self):
        pass
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_remember = collections.Counter(s)
        result = []
        for c in s:
            if c not in result:
                while(result and c < result[-1] and dict_remember[result[-1]] > 0):
                    result.pop()
                result.append(c)
            dict_remember[c] -= 1
            print(dict_remember)
            print(result)
        return ''.join(result)

        


test = Solution()
print(test.removeDuplicateLetters('cbacdcbc'))