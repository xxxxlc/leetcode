# 给你两个正整数数组 nums 和 target ，两个数组长度相等。

# 在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且：

# 令 nums[i] = nums[i] + 2 且
# 令 nums[j] = nums[j] - 2 。
# 如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。

# 请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。


class Solution(object):
    def makeSimilar(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        nums.sort()
        target.sort()

        j = [0, 0]
        ans = 0
        for x in nums:
            p = x % 2
            while (target[j[p]] % 2 != p):
                j[p] += 1
            ans += abs(x - target[j[p]])    
            j[p] += 1
        return ans // 4


nums = [8,12,6]
target = [2,14,10]
a = Solution()
print(a.makeSimilar(nums, target))