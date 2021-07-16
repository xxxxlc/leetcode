# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

# 求所能获得硬币的最大数量。

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points = [0] * (len(nums) + 2)
        points[0] = points[-1] = 1
        for i in range(1, len(nums) + 1):
            points[i] = nums[i - 1]
        
        dp = [[0 for i in range(len(nums) + 2)] for j in range(0, len(nums) + 1)]
        print(dp)
        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(points)):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i]*points[k]*points[j])
        
        return dp[0][len(points) - 1]


nums = [3,1,5,8]
a = Solution()
print(a.maxCoins(nums))