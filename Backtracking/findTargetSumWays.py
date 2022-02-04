# 给你一个整数数组 nums 和一个整数 target 。

# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

class Solution(object):
    def findTargetSumWays_backtrack(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.ans = 0
        self.backtrack(nums, target, 0, 0)
        return self.ans

    def backtrack(self, nums, target, sum_nums, index):
        if index == len(nums):
            if sum_nums == target:
                self.ans += 1
            return
        
        self.backtrack(nums, target, sum_nums + nums[index], index + 1)
        self.backtrack(nums, target, sum_nums - nums[index], index + 1)

    def findTargetSumWays(self, nums, target):
        sum_all = sum(nums)

        diff = sum_all - target

        if diff < 0 or diff % 2 != 0:
            return 0
        
        neg = int(diff / 2)

        dp = [0] * (neg + 1)
        dp[0] = 1
        for i in range(0, len(nums)):
            for j in range(neg, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[neg] 
            
nums = [1,1,1,1,1]
target = 3

a = Solution()
print(a.findTargetSumWays(nums, target))
