# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的 子数组 中满足 元素最小公倍数为 k 的子数组数目。

# 子数组 是数组中一个连续非空的元素序列。

# 数组的最小公倍数 是可被所有数组元素整除的最小正整数。

from math import gcd
class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(n):
            if k % nums[i] != 0:
                continue

            g = 1

            for j in range(i, n):
                g = self.gys(g, nums[j])
                if g == k:
                    ans += 1
        return ans

        
    def gys(self, a, b):
        remainder = gcd(a, b)
        return a * b // remainder

nums = [3]
k = 2

a = Solution()
print(a.subarrayLCM(nums, k))