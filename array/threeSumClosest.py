# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

# 返回这三个数的和。

# 假定每组输入只存在恰好一个解。


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        distant = float('inf')
        ans = None

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = len(nums) - 1
            j = i + 1
            
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return temp
                if (abs(temp - target) < distant):
                    distant = abs(temp - target)
                    ans = temp
                if temp > target:
                    while j < k - 1 and nums[k - 1] == nums[k]:
                        k = k - 1
                    k = k - 1
                else:
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
        
        return ans


nums = [3,4,5,5,7]
target = 13

a = Solution()
print(a.threeSumClosest(nums, target))