# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

#  

# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = collections.Counter(nums)
        ans = []
        for key in d.keys():
            if d[key] == 1:
                ans.append(key)
        return ans


nums = [1,2,1,3,2,5]
a = Solution()

print(a.singleNumber(nums))
