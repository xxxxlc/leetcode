# 给你一个整数数组 nums ，返回全部为 0 的 子数组 数目。

# 子数组 是一个数组中一段连续非空元素组成的序列。


class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        ans = 0

        zeroLength = 0

        while (i < len(nums)):
            ans += zeroLength
            if nums[i] == 0:
                zeroLength += 1
            else:
                zeroLength = 0
            i += 1
        if zeroLength != 0:
            ans += zeroLength
        return ans
    



nums = [1,3,0,0,2,0,0,4]

a = Solution()
print(a.zeroFilledSubarray(nums))