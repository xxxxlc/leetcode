# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的子数组中元素的最大公因数等于 k 的子数组数目。

# 子数组 是数组中一个连续的非空序列。

# 数组的最大公因数 是能整除数组中所有元素的最大整数。

from math import gcd


class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] % k != 0:
                continue
            g = 0
            for j in range(i, n):
                g = gcd(nums[j], g)
                if g == k:
                    ans += 1
        return ans


nums = [3,3,4,1,2]
k = 1

a = Solution()
print(a.subarrayGCD(nums, k))