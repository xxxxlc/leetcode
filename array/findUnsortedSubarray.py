# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 请你找出符合题意的 最短 子数组，并输出它的长度

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nmin = float('inf')
        left = -1
        nmax = float('-inf')
        right = -1

        for i in range(n):
            if nmax > nums[i]:
                right = i
            else:
                nmax = nums[i]
            
            if nmin < nums[n - 1 - i]:
                left = n - 1 - i
            else:
                nmin = nums[n - 1 -i]

        if right == -1:
            return 0

        return right - left + 1


nums = [2,6,4,8,10,9,15]
a = Solution()
print(a.findUnsortedSubarray(nums))
