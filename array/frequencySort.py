# 给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。

# 返回 已排序的字符串 。如果有多个答案，返回其中任何一个。

import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.Counter(s)
        d = sorted(d.items(), key=lambda d : d[1], reverse=True)
        
        ans = ""

        for i in range(len(d)):
            for _ in range(d[i][1]):
                ans += d[i][0]

        return ans

s = "Aabb"

a = Solution()
print(a.frequencySort(s))
