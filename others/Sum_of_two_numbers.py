# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

class Solution(object):

    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        for i,element in enumerate(nums):
            try:
                index_another = nums.index(target - element)
                if i != index_another:
                    return [i, index_another]
            except:
                pass

a = Solution()
nums = [2, 7, 11, 15]
target = 9
print(a.twoSum(nums, target))


