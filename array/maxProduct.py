# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dt = [0] * (len(nums) + 1)
        dp[0] = 1
        dt[0] = 1

        for i in range(0, len(nums)):
            dp[i + 1] = max(dp[i] * nums[i], dt[i] * nums[i], nums[i])
            dt[i + 1] = min(dt[i] * nums[i], dp[i] * nums[i], nums[i])
        
        return max(dp[1:])


nums = [-2,0,-1]
a = Solution()
print(a.maxProduct(nums))