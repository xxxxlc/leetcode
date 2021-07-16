# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumnums = 0
        for i in nums:
            sumnums += i
        if sumnums % 2 != 0:
            return False
        sumnums = int(sumnums / 2)

        dp =  [[False for col in range(sumnums + 1)] for row in range(len(nums) + 1)]
        for i in range(0, len(nums)):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, sumnums + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(nums)-1][sumnums]


nums = [1,2,5]
a = Solution()
print(a.canPartition(nums))
