# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [0] * (len(nums) + 1)
        next = [0] * (len(nums) + 1)
        pre[0] = 1
        next[len(nums)] = 1 
        for i in range(0, len(nums)):
            pre[i + 1] = pre[i] * nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            next[i] = next[i + 1] * nums[i]
        
        ans = [0] * len(nums)
        for i in range(1, len(nums) + 1):
            ans[i - 1] = pre[i - 1] * next[i]

        return ans

nums = [1,0,3,4]
a = Solution()
print(a.productExceptSelf(nums))