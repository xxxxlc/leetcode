# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
        ans = 1
        for i in range(0, len(b)):
            ans = pow(ans, 10, MOD) * pow(a, b[i], MOD) % MOD
        return ans


s = 2
b = [1, 0]

a = Solution()
print(a.superPow(s , b))