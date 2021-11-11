# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列

class Solution(object):
    def permuteUnique(self, nums):
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
            if track not in self.res:
                self.res.append(track[:])
            return 
        
        for i in range(len(nums)):
            track.append(nums[i])
            self.backtrack(track, nums[:i] + nums[i+1:])
            track.pop(-1)



nums = [1,1,2]
a = Solution()
print(a.permuteUnique(nums))