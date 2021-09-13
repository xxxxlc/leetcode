# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        pos = None
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                pos =  mid
                break
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

        if l > r and not pos:
            return [-1, -1]
        l = pos
        while(l >= 0 and nums[l] == target):
            l = l - 1
        r = pos
        while(r < len(nums) and nums[r] == target):
            r = r + 1
        
        return [l + 1, r - 1]

        


nums = [1]
target = 1

a = Solution()
print(a.searchRange(nums, target))
