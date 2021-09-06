# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须 原地 修改，只允许使用额外常数空间。



class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        turn = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i - 1 
                turn = True
                break
        if turn == False:
            return nums[::-1]
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[index]:
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp
                nums[index+1:] = reversed(nums[index+1:])
                break

        return nums

nums = [2,3,1]

a = Solution()
print(a.nextPermutation(nums))