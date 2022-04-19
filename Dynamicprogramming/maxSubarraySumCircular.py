# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。

# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。

# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = cur = float('-inf')

        for x in nums:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        rightsum = [float('-inf')] * len(nums)
        rightsum[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            rightsum[i] = rightsum[i + 1] + nums[i]

        maxright = [float('-inf')] * len(nums)
        maxright[-1] = rightsum[-1]
        for i in range(len(nums) - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsum[i])
        
        leftsum = 0
        for i in range(len(nums) - 2):
            leftsum += nums[i]
            ans = max(ans, leftsum + maxright[i + 2])
        return ans

nums = [1,-2,3,-2]
a = Solution()
print(a.maxSubarraySumCircular(nums))