# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。你的 起始分数 为 0 。

# 在一步 操作 中：

# 选出一个满足 0 <= i < nums.length 的下标 i ，
# 将你的 分数 增加 nums[i] ，并且
# 将 nums[i] 替换为 ceil(nums[i] / 3) 。
# 返回在 恰好 执行 k 次操作后，你可能获得的最大分数。

# 向上取整函数 ceil(val) 的结果是大于或等于 val 的最小整数。

import math
import heapq
class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # nums.sort()
        heap = [-x for x in nums]
        heapq.heapify(heap)

        n = 0

        ans = 0

        while(n < k):

            cur = - heapq.heappop(heap)

            ans += cur

            cur = - math.ceil(cur / 3)

            heapq.heappush(heap, cur)

            n += 1

        return ans 






nums = [1,10,3,3,3]

k = 3

a = Solution()
print(a.maxKelements(nums, k))