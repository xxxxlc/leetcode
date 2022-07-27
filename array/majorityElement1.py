# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        c = n // 3 + 1

        d = collections.Counter(nums)
        return [key for key, value in d.items() if value >= c]




nums = [3,2,3]

a = Solution()
print(a.majorityElement(nums))