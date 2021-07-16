# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = dict()
        presum[0] = 1
        sum_i = 0
        ans = 0
        for i in range(0, len(nums)):
            sum_i += nums[i]
            sum_j = sum_i - k

            if sum_j in presum:
                ans += presum[sum_j]
            
            presum[sum_i] = presum.get(sum_i, 0) + 1
        
        return ans


nums = [1,1,1]
k = 2
a = Solution()
print(a.subarraySum(nums, k))