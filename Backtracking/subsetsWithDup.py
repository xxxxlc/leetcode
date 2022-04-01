# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.ans = []
        self.backtrack([], nums, 0)
        return self.ans

    def backtrack(self, track, nums, idx):
        if track not in self.ans:
            self.ans.append(track[:])

        for i in range(idx, len(nums)):
            self.backtrack(track + [nums[i]], nums, i + 1)
        

nums = [4,4,4,1,4]
a = Solution()
print(a.subsetsWithDup(nums))