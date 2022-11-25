# 给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。

# 如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：

# s 被分成 k 段互不相交的子字符串。
# 每个子字符串长度都 至少 为 minLength 。
# 每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。质数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。
# 请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 109 + 7 取余 后的结果。

# 一个 子字符串 是字符串中一段连续字符串序列。


class Solution(object):
    def beautifulPartitions(self, s, k, minLength):
        """
        :type s: str
        :type k: int
        :type minLength: int
        :rtype: int
        """
        def can_partition(j):
            return j == 0 or j == self.n or not self.is_prime(s[j - 1]) and self.is_prime(s[j])
        
        MOD = 10** 9 + 7
        self.n = len(s)
        n = len(s)
        if  k * minLength > n or not self.is_prime(s[0]) or self.is_prime(s[-1]):
            return 0
        f = [[0] * (n + 1) for _ in range(k + 1)]

        f[0][0] = 1

        for i in range(1, k + 1):
            tot = 0
            for j in range(i * minLength, n - (k - i) * minLength + 1):
                if can_partition(j - minLength):
                    tot = (tot + f[i-1][j-minLength]) % MOD
                if can_partition(j):
                    f[i][j] = tot
        
        return f[k][n]

    def is_prime(self, c):
        return c in "2357"




s = "23542185131"
k = 3
minLength = 2

a = Solution()
print(a.beautifulPartitions(s, k, minLength))
