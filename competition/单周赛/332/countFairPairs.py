# 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。

# 如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：

# 0 <= i < j < n，且
# lower <= nums[i] + nums[j] <= upper

from typing import List
import heapq

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n):
            j = bisect_right(nums, upper - nums[i], i + 1, n)
            k = bisect_left(nums, lower - nums[i], i + 1, n)
            count += (j - k)
        return count




nums = [0,1,7,4,4,5]
lower = 3
upper = 6

a = Solution()
print(a.countFairPairs(nums, lower, upper))