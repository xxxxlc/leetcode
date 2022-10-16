# 给你一个整数数组 nums 和两个整数 minK 以及 maxK 。

# nums 的定界子数组是满足下述条件的一个子数组：

# 子数组中的 最小值 等于 minK 。
# 子数组中的 最大值 等于 maxK 。
# 返回定界子数组的数目。

# 子数组是数组中的一个连续部分。

class Solution(object):


    def countSubarrays(self, nums, minK, maxK):
        ans = 0
        min_i = max_i = i0 = -1

        for i, x in enumerate(nums):
            if x == minK: min_i = i
            if x == maxK: max_i = i
            
            if not minK <= x <= maxK: i0 = i

            ans += max(min(min_i, max_i) - i0, 0)
        return ans

    """
    超时做法
    """
    def countSubarrays1(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        n = len(nums)

        dp = [[[float('inf'), float('-inf')] for _ in range(n)] for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j][0] = nums[j]
                    dp[i][j][1] = nums[j]
                else:
                    dp[i][j][0] = min(dp[i][j - 1][0], nums[j])
                    dp[i][j][1] = max(dp[i][j - 1][1], nums[j])

                if dp[i][j][0] == minK and dp[i][j][1] == maxK:
                    ans += 1
        
        return ans
        



nums = [1,3,5,2,7,5]
minK = 1
maxK = 5

a = Solution()
print(a.countSubarrays(nums, minK, maxK))