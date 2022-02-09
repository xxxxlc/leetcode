# 给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。

# |x| 的值定义为：

# 如果 x >= 0 ，那么值为 x 。
# 如果 x < 0 ，那么值为 -x 。

from sympy import solve


class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans

nums = [1,2,2,1]
k = 1

a = Solution()
print(a.countKDifference(nums, k))