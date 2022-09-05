# 给你一个由 正 整数组成的数组 nums 。

# 如果 nums 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。

# 返回 最长 的优雅子数组的长度。

# 子数组 是数组中的一个 连续 部分。

# 注意：长度为 1 的子数组始终视作优雅子数组。

class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxLength = [1] * len(nums)
        maxNum = nums[:]

        for i in range(len(nums)):
            if i == 0:
                maxNum[0] = nums[i]
            else:
                for j in range(i - 1, -1, -1):
                    if nums[i] & maxNum[j] == 0:
                        if maxLength[i] < maxLength[j] + 1:
                            maxLength[i] = maxLength[j] + 1
                            maxNum[i] = maxNum[j] | nums[j]  
         
        return max(maxLength)
                         


nums = [362928166,741516746,281289675,373804929,67108866,33554432,273154048,653530653,6278896,721906935]

a = Solution()
print(a.longestNiceSubarray(nums))