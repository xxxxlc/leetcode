# 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。

# 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * n
        num = 1

        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while(num % 10 == 9 or num + 1 > n):
                    num //= 10
                num += 1
        return ans 






n = 13

a = Solution()
print(a.lexicalOrder(n))