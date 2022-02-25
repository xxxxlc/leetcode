# 给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if nums:
            k = k % len(nums)
            nums[:]=nums[-k:]+nums[:-k]

        return nums


nums = [1,2,3,4,5,6,7]
k = 3

a = Solution()
print(a.rotate(nums, k))