# 给定一个正整数数组 nums和整数 k 。

# 请找出该数组内乘积小于 k 的连续的子数组的个数。

from turtle import left


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        ans = 0

        left = 0
        prod = 1

        for right in range(len(nums)):
            prod *= nums[right]
            while (prod >= k):
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        return ans


nums = [10,5,2,6]
k = 0

a = Solution()
print(a.numSubarrayProductLessThanK(nums, k))