# 给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：

# 删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
# 删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
# 请你返回纸上能写出的字典序最小的字符串。

import collections

class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        cnt = collections.Counter(s)

        minEle = 0
        st = []

        for c in s:
            cnt[c] -= 1

            while minEle < 25 and cnt[chr(minEle + 97)] == 0:
                minEle += 1
            st.append(c)

            while st and st[-1] <= chr(minEle + 97):
                ans.append(st.pop())
        return ''.join(ans)


s = "bac"
a = Solution()
print(a.robotWithString(s))
