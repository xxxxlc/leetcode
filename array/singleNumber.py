# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = collections.Counter(nums)

        for key in a.keys():
            if a[key] == 1:
                return a


nums = [0,1,0,1,0,1,99]

a = Solution()
print(a.singleNumber(nums))