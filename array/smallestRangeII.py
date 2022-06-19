# 给你一个整数数组 nums，和一个整数 k 。

# 对于每个下标 i（0 <= i < nums.length），将 nums[i] 变成 nums[i] + k 或 nums[i] - k 。

# nums 的 分数 是 nums 中最大元素和最小元素的差值。

# 在更改每个下标对应的值之后，返回 nums 的最小 分数 。

class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)

        minNum = nums[0]
        maxNum = nums[-1]

        ans = maxNum - minNum

        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            ans = min(ans, max(maxNum - k, a + k) - min(minNum + k, b - k))

        return ans


nums = [1,3,6]
k = 3

a = Solution()
print(a.smallestRangeII(nums, k))
