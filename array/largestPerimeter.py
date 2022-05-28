# 给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        return next((nums[i] + nums[i - 1] + nums[i - 2] for i in range(len(nums) - 1, 1, -1) if nums[i] - nums[i - 1] < nums[i - 2]), 0)

nums = [1,2,1]

a = Solution()
print(a.largestPerimeter(nums))