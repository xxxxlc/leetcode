# 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。

# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。

# 返回一对观光景点能取得的最高分。


class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        ans = 0
        mx = values[0] + 0

        for i in range(1, n):
            ans = max(ans, values[i] - i + mx)
            mx = max(mx, values[i] + i)
        
        return ans


values = [8,1,5,2,6]

a = Solution()
print(a.maxScoreSightseeingPair(values))