# 给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。

# 注意： x 不必 是 nums 的中的元素。

# 如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。


class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        left = 0
        right = n

        while (left <= right):
            mid = left + (right - left) // 2
            cmp = self.isSpecial(mid, nums)
            if cmp == 0:
                return mid
            elif cmp > 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    
    def isSpecial(self, x, nums):
        t = sum(nums[i] >= x for i in range(len(nums)))
        
        return t - x


nums = [3,5]

a = Solution()
print(a.specialArray(nums))