# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        track = []
        self.backtrack(nums, 0, track)
        return self.res

    def backtrack(self, nums, start, track):
        self.res.append(track[:])

        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop(-1)

nums = [1,2,3]
a = Solution()
print(a.subsets(nums))

