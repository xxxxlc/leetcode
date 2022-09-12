# 给定一个长度为 n 的整数数组 nums 。

# 假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：

# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
# 返回 F(0), F(1), ..., F(n-1)中的最大值 。

# 生成的测试用例让答案符合 32 位 整数。


class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sum(nums)
        F0 = 0
        for i in range(len(nums)):
            F0 += i * nums[i]
        maxF = F0
        for i in range(1, len(nums)):
            Fnext = F0 + n - nums[len(nums) - i] * (len(nums))
            maxF = max(maxF, Fnext)
            F0 = Fnext
        
        return maxF

nums = [4,3,2,6]

a = Solution()
print(a.maxRotateFunction(nums))