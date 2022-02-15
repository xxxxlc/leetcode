# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

# 请你找出并返回只出现一次的那个数。

# 你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while(left < right):
            mid = (left + right) // 2

            if mid % 2 == 0:
                if nums[mid] != nums[mid + 1]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] != nums[mid - 1]:
                    right = mid
                else:
                    left = mid + 1
        
        return nums[left]


nums = [1,1,2,3,3,4,4,8,8]

a = Solution()
print(a.singleNonDuplicate(nums))