# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。

# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。

# 返回可能的 最小差值 。



class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        min_ans = float('inf')
        for i in range(0, len(nums) - k + 1):
            if min_ans > nums[i + k - 1] - nums[i]:
               min_ans = nums[i + k - 1] - nums[i]

        return min_ans 


nums = [9,4,1,7]
k = 2

a = Solution()
print(a.minimumDifference(nums, k))