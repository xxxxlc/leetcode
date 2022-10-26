# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。

# 子数组 是数组中 连续 的一部分。


from collections import deque


class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = len(nums) + 1
        preSum = [0]
        preSum.extend(preSum[i] + nums[i] for i in range(len(nums)))

        q = deque()
        for i, cur_s in enumerate(preSum):
            while q and cur_s - preSum[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and preSum[q[-1]] >= cur_s:
                q.pop()
            q.append(i)
        return ans if ans < len(nums) + 1 else -1

        




nums = [48,99,37,4,-31]
k = 140

a = Solution()
print(a.shortestSubarray(nums, k))