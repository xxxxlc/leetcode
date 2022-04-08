# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

# 子数组 是数组中的一个连续序列。

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0, 0] for _ in range(len(nums))]

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = dp[i - 1][1] + dp[i][0]
        
        return dp[len(nums) - 1][1]


nums = [1,2,3,4,5,6,4,5,6,7,8]

a = Solution()
print(a.numberOfArithmeticSlices(nums))