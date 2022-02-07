# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

# 请你返回 nums 中唯一元素的 和

import collections
from itertools import count


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element = collections.Counter(nums)
        ans = 0
        for num, count in element.items():
            if count == 1:
                ans += num
        return ans
        

nums = [1,2,3,2]

a = Solution()
print(a.sumOfUnique(nums))