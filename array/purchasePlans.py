# 小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

# 注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1


class Solution(object):
    def purchasePlans(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)

        ans = 0

        i = 0
        j = len(nums) - 1

        while (i < len(nums) and i < j):
            cur = nums[i]
            find = target - cur
            while (j > i and nums[j] > find):
                j = j - 1
            ans += j - i
            i += 1
        
        return ans % 1000000007


nums = [2,5,3,5]
target = 6

a = Solution()
print(a.purchasePlans(nums, target))
