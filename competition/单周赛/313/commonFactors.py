
# 给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。

# 如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。


class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = 0

        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        
        return ans

a = 25
b = 1

c = Solution()
print(c.commonFactors(a, b))
