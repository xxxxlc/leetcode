# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return False
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                continue
            s1 = set()
            for j in range(i + 1, len(nums)):
                if nums[j] in s1:
                    continue
                if nums[i] >= nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
                s1.add(nums[j])
            s.add(nums[i])
        
        return False
                    

nums = [1,5,0,4,1,3]

a = Solution()
print(a.increasingTriplet(nums))
