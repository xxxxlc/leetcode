# 给你一个字符串 s 和一个 正 整数 k 。

# 从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：

# 每个子字符串的长度 至少 为 k 。
# 每个子字符串是一个 回文串 。
# 返回最优方案中能选择的子字符串的 最大 数目。

# 子字符串 是字符串中一个连续的字符序列。

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        f = [0] * (n + 1)

        for i in range(2 * n - 1):
            l = i // 2
            r = l + i % 2

            f[l + 1] = max(f[l], f[l + 1])

            while(l >= 0 and r < n and s[l] == s[r]):
                if r - l + 1 >= k:
                    f[r + 1] = max(f[r + 1], f[l] + 1)
                l -= 1
                r += 1

        return f[n]


    


    
s = "abaccdbbd"
k = 3

a = Solution()
print(a.maxPalindromes(s, k))
