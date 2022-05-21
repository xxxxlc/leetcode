# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementNum = 1
        length = len(nums)
        i = 1
        while(i < length):
            if nums[i] == nums[i - 1]:
                elementNum += 1
                if elementNum > 2:
                    for j in range(i, len(nums) - 1):
                        nums[j] = nums[j + 1]
                    length -= 1
                    elementNum = 2
                    continue
            else:
                elementNum = 1
            i += 1
        
        return length

nums = [1,1,1,2,2,3]

a = Solution()
print(a.removeDuplicates(nums))