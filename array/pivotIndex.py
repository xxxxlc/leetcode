# 给你一个整数数组 nums ，请计算数组的 中心下标 。

# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [0] * len(nums)
        right = [0] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] + nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] + nums[i + 1]

        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        return -1

nums = [1, 7, 3, 6, 5, 6]

a = Solution()
print(a.pivotIndex(nums))
