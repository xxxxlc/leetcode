# 给你一个 不包含 任何零的整数数组 nums ，找出自身与对应的负数都在数组中存在的最大正整数 k 。

# 返回正整数 k ，如果不存在这样的整数，返回 -1 。


class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        positive = set()
        negetivie = set()

        for num in nums:
            if num < 0:
                negetivie.add(num)
            else:
                positive.add(num)
        
        for num in positive:
            if -num in negetivie:
                ans = max(ans, num)
        return -1 if ans == 0 else ans


nums = [-1,10,6,7,-7,1]

a = Solution()
print(a.findMaxK(nums))