# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.size = len(nums)
        track = []
        self.backtrack(track, nums)
        return self.res


    def backtrack(self, track, nums):
        if len(track) == self.size:
            self.res.append(track[:])
            return 
        
        for i in nums:
            if i in track:
                continue
            track.append(i)
            self.backtrack(track, nums)
            track.pop(-1)


nums = [1,2,3]
a = Solution()
print(a.permute(nums))