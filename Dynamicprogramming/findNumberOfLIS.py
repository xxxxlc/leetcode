# 给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。

# 注意 这个数列必须是 严格 递增的。

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        cnt = [0] * len(nums)

        maxlength = 0
        ans = 0

        for i in range(len(nums)):
            dp[i] = 1
            cnt[i] = 1

            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > maxlength:
                maxlength = dp[i]
                ans = cnt[i]
            elif dp[i] == maxlength:
                ans += cnt[i]
        
        return ans


nums = [2,2,2,2,2]

a = Solution()
print(a.findNumberOfLIS(nums))