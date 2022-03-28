# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums) + 1

        left = sums = 0

        for right in range(len(nums)):
            sums += nums[right]
            while (sums >= target):
                ans = min(ans, right - left + 1)
                sums -= nums[left]
                left += 1
        
        if ans == len(nums) + 1:
            return 0

        return ans


target = 11
nums = [1,1,1,1,1,1,1,1]

a = Solution()
print(a.minSubArrayLen(target, nums))