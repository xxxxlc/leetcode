# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 假设你总是可以到达数组的最后一个位置。


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] + j  >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[len(nums) - 1]
                



nums = [2,3,0,1,4]
a = Solution()
print(a.jump(nums))