# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = nums + [len(nums) + 1] * 2
        for i in range(len(nums) - 1):
            nums[abs(nums[i])] = -abs(nums[abs(nums[i])])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return i

nums = [2,0]

a = Solution()
print(a.missingNumber(nums))