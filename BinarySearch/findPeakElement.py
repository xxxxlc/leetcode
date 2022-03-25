# 峰值元素是指其值严格大于左右相邻值的元素。

# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

# 你可以假设 nums[-1] = nums[n] = -∞ 。

# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = len(nums) - 1

        def get(c):
            return float('-inf') if c in [-1, n] else nums[c]

        while(left <= right):
            mid = left + (right - left) // 2

            if get(mid - 1) < get(mid) and get(mid) > get(mid + 1):
                return mid
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
                
        
        return left
            


nums = [1,2]

a = Solution()
print(a.findPeakElement(nums))
