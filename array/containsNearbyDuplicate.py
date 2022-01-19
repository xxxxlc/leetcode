# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，
# 满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # for i in range(0, len(nums)):
        #     n = min(len(nums), i + k + 1)
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False


nums = [1,2,3,1,2,3]
k = 2

a = Solution()
print(a.containsNearbyDuplicate(nums, k))
