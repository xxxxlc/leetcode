# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0

        while(fast < len(nums)):
            while(nums[fast] == 0):
                if fast >= len(nums) - 1:
                    break
                fast += 1
            
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        
        nums[slow:] = [0] * (len(nums) - slow)

        return nums

nums = [0]
a = Solution()

print(a.moveZeroes(nums))