# 给你一个整数数组 nums ，你可以对它进行一些操作。

# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = max(nums)
        total = [0] * (maxVal + 1)

        for val in nums:
            total[val] += val
        
        temp1, temp2 = total[0], max(total[0], total[1])

        for i in range(2, len(total)):
            temp1, temp2 = temp2, max(temp1 + total[i], temp2)

        return temp2

nums = [2,2,3,3,3,4]
a = Solution()
print(a.deleteAndEarn(nums))