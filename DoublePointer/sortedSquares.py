# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)

        left = 0
        right = len(nums) - 1

        point = len(nums) - 1

        while(left <= right):
            if abs(nums[left]) > abs(nums[right]):
                ans[point] = nums[left] ** 2
                point -= 1
                left += 1
            else:
                ans[point] = nums[right] ** 2
                point -= 1
                right -= 1
        
        return ans


nums = [-4,-1,0,3,10]

a = Solution()
print(a.sortedSquares(nums))