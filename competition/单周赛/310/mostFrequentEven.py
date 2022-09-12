# 给你一个整数数组 nums ，返回出现最频繁的偶数元素。

# 如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。


class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        minElement = -1
        freq = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                d[nums[i]] = d.get(nums[i], 0) + 1
                if freq == d[nums[i]]:
                    if minElement > nums[i]:
                        minElement = nums[i]
                elif freq < d[nums[i]]:
                    minElement = nums[i]
                    freq = d[nums[i]]
        
        return minElement

        



nums = [29,47,21,41,13,37,25,7]
a = Solution()
print(a.mostFrequentEven(nums))