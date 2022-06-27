# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

# 请返回 nums 的动态和。

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        ans[0] = nums[0]
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] + nums[i]
        return ans

nums = [1,2,3,4]

a = Solution()
print(a.runningSum(nums))