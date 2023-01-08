# 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。

# 你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。


from collections import Counter

class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        j = n = len(s)

        ct = Counter()

        while ct['a'] < k or ct['b'] < k or ct['c'] < k:
            if j == 0:
                return -1
            j -= 1
            ct[s[j]] += 1
        

        ans = n - j

        for i, chr in enumerate(s):
            ct[chr] += 1
            while j < n and ct[s[j]] > k:
                ct[s[j]] -= 1
                j += 1
            ans = min(ans, i + 1 + n - j)
            if j == n:
                break
        
        return ans

                





s = "cbbac"
k = 1

a = Solution()
print(a.takeCharacters(s, k))