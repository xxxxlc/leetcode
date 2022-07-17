# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

# 如果存在则返回 true，不存在返回 false。


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        i = 0
        j = k
        
        while(j < len(nums)):
            for m in range(i, j + 1):
                for n in range(m + 1, j + 1):
                    if abs(nums[m] - nums[n]) <= t:
                        return True
            i += 1
            j += 1
        return False



nums = [1,2,3,1]
k = 3
t = 0

a = Solution()
print(a.containsNearbyAlmostDuplicate(nums, k, t))