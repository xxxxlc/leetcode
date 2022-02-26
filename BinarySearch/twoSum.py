# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

# 你所设计的解决方案必须只使用常量级的额外空间


from turtle import left


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            idx = self.search(numbers, target - numbers[i], i + 1)

            if idx != -1 and idx != i:
                return [i + 1, idx + 1]
    
    def search(self, nums, target, left):
        right = len(nums) - 1

        while(left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1

numbers = [1,2,3,4,4,9,56,90]
target = 8

a = Solution()
print(a.twoSum(numbers, target))