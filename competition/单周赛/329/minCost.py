# 给你一个整数数组 nums 和一个整数 k 。

# 将数组拆分成一些非空子数组。拆分的 代价 是每个子数组中的 重要性 之和。

# 令 trimmed(subarray) 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。

# 例如，trimmed([3,1,2,4,3,4]) = [3,4,3,4] 。
# 子数组的 重要性 定义为 k + trimmed(subarray).length 。

# 例如，如果一个子数组是 [1,2,3,3,3,4,4] ，trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4] 。这个子数组的重要性就是 k + 5 。
# 找出并返回拆分 nums 的所有可行方案中的最小代价。

# 子数组 是数组的一个连续 非空 元素序列。

from typing import List

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)

        f = [0] * (n + 1)

        for i in range(n):
            # 子数组的特征值
            t = 0

            # 每个数的个数
            cnt = [0] * n 

            # 最小值
            mn = float('inf')
            for j in range(i, -1, -1):
                x = nums[j]
                cnt[x] += 1

                if cnt[x] == 2:
                    t += 2
                elif cnt[x] > 2:
                    t += 1

                mn = min(mn, f[j] + t)
            f[i + 1] = k + mn 
        
        return f[n]
                



nums = [1,2,1,2,1,3,3]
k = 2

a = Solution()
print(a.minCost(nums, k))