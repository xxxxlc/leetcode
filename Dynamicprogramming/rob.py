# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 2)

        # for i in range(len(nums)-1, -1, -1):
        #     dp[i] = max(dp[i+1], nums[i] + dp[i+2])

        # return dp[0]

        for i in range(2, len(nums) + 2):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])

        return dp[len(nums)+1]


nums = [2,7,9,3,1]
a = Solution()
print(a.rob(nums))