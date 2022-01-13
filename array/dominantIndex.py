# 给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。

# 请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        index = nums.index(max(nums))
        nums = sorted(nums)
        if nums[-1] >= 2 * nums[-2]:
            return index
        return -1

a = Solution()
nums = [3,6,1,0]
print(a.dominantIndex(nums))