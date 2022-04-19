# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

# 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

# 请你返回乘积为正数的最长子数组长度。

class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            if nums[0] > 0:
                return 1
            else:
                return 0

        dp = [0] * (len(nums))
        dt = [0] * (len(nums))

        if nums[0] > 0:
            dp[0] = 1
        elif nums[0] < 0:
            dt[0] = 1

        ans = 0

        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[i] = 0
                dt[i] = 0
            elif nums[i] > 0:
                dp[i] = dp[i - 1] + 1
                dt[i] = dt[i - 1] + 1 if dt[i - 1] > 0 else 0
            else:
                dp[i] = dt[i - 1] + 1 if dt[i - 1] > 0 else 0
                dt[i] = dp[i - 1] + 1
            ans = max(ans, dp[i])
        
        return ans




nums = [-1,-2,-3,0,1]

a = Solution()
print(a.getMaxLen(nums))