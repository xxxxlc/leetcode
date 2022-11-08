# 给你一个由正整数组成的整数数组 nums ，返回其中可被 3 整除的所有偶数的平均值。

# 注意：n 个元素的平均值等于 n 个元素 求和 再除以 n ，结果 向下取整 到最接近的整数。

class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        ans = 0

        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                ans += i
                n += 1
        if n == 0:
            return 0
        return ans // n


nums = [1,3,6,10,12,15]
a = Solution()

print(a.averageValue(nums))