# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

# 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        # memo = dict()
        # def dp(k, n):
        #     if k == 1: return n
        #     if n == 0: return 0
        #     res = float('inf')
        #     # if (k, n) in memo:
        #     #     return memo[(k, n)]
        #     # for i in range(1, n + 1):
        #     #     res = min(res, max(dp(k - 1, i - 1), dp(k, n - i)) + 1)

        #     lo, hi = 1, n
        #     while lo <= hi:
        #         mid = lo + (hi - lo) // 2
        #         broken = dp(k - 1, mid - 1)
        #         not_broken = dp(k, n - mid)
        #         if broken > not_broken:
        #             hi = mid - 1
        #             res = min(res, broken + 1)
        #         else:
        #             lo = mid + 1
        #             res = min(res, not_broken + 1)

        #     memo[(k, n)] = res
        #     return res
        
        # return dp(k, n)

        dp = [[0 for i in range(0, n + 1)] for egg in range(0, k + 1)]
        m = 0
        while (dp[k][m] < n):
            m = m + 1
            for i in range(1, k + 1):
                dp[i][m] = dp[i - 1][m - 1] + 1 + dp[i][m - 1]
        
        return m



a = Solution()
k = 3
n = 14
print(a.superEggDrop(k, n))