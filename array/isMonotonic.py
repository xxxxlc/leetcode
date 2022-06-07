# 如果数组是单调递增或单调递减的，那么它是 单调 的。

# 如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums 是单调递减的。

# 当给定的数组 nums 是单调数组时返回 true，否则返回 false。

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        symbol = None
        for i in range(0, len(nums) - 1):
            c = nums[i + 1] - nums[i]
            if c != 0 and symbol is None:
                symbol = c
            else:
                if c == 0:
                    continue
                if symbol * c < 0:
                    return False
        return True





nums = [11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]

a = Solution()
print(a.isMonotonic(nums))
