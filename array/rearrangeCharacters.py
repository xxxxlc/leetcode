# 给你两个下标从 0 开始的字符串 s 和 target 。你可以从 s 取出一些字符并将其重排，得到若干新的字符串。

# 从 s 中取出字符并重新排列，返回可以形成 target 的 最大 副本数。


from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        d1 = Counter(target)
        d2 = Counter(s)

        ans = float('inf')

        for key, val in d1.items():
            if key not in d2.keys():
                return 0

            ans = min(d2[key] // d1[key], ans)
        
        return ans






s = "ilovecodingonleetcode"
target = "code"

a = Solution()
print(a.rearrangeCharacters(s, target))