# 给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。

# 统计并返回 num 中的 中位数 等于 k 的非空子数组的数目。

# 注意：

# 数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
# 例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
# 子数组是数组中的一个连续部分。

from collections import Counter

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        pos = nums.index(k)

        cnt = Counter()

        cnt[0] = 1

        c = 0

        for i in range(pos + 1, len(nums)):
            c += 1 if nums[i] > k else -1
            cnt[c] += 1

        c = 0

        ans = cnt[0] + cnt[1]

        for i in range(pos - 1, -1, -1):
            c += -1 if nums[i] > k else 1
            ans += cnt[c] + cnt[c+1]

        return ans



        


nums = [3,2,1,4,5]
k = 4

a = Solution()
print(a.countSubarrays(nums, k))