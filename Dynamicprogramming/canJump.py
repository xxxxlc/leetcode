# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标。

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(0, len(nums)):
            if dp[i] == True:
                if i + nums[i] < len(nums):
                    for j in range(i + 1, i + nums[i] + 1):
                        dp[j] = True
                else:
                    return True
        
        return dp[len(nums) - 1]


nums = [2, 0]
a = Solution()
print(a.canJump(nums))