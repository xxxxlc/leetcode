# 给你两个字符串 s 和 t 。

# 你可以从字符串 t 中删除任意数目的字符。

# 如果没有从字符串 t 中删除字符，那么得分为 0 ，否则：

# 令 left 为删除字符中的最小下标。
# 令 right 为删除字符中的最大下标。
# 字符串的得分为 right - left + 1 。

# 请你返回使 t 成为 s 子序列的最小得分。

# 一个字符串的 子序列 是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说 "ace" 是 "abcde" 的子序列，但是 "aec" 不是）。

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        suf = [m] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                j -= 1
            suf[i] = j + 1
        
        ans = suf[0]

        j = 0
        for i, c in enumerate(s):
            if c == t[j]:
                j += 1

                if suf[i + 1] >= j:
                    ans = min(ans, suf[i+1] - j)
                
                if j == m:
                    break
        
        return ans



s = "abacaba"
t = "bzaa"

a = Solution()
print(a.minimumScore(s, t))