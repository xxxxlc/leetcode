# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        false_list = []
        for index,char in enumerate(s):
            if char not in s[index+1:] and char not in false_list:
                print(s[index+1:])
                return index
            false_list.append(char)
        return -1

a = Solution()
s = 'cc'
print(a.firstUniqChar(s))