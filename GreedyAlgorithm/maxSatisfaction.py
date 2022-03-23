# 一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。

# 一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i] 。

# 请你返回做完所有菜 「喜爱时间」总和的最大值为多少。

# 你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        s = sorted(satisfaction, reverse=True)
        s_sum = 0
        ans = 0
        for i in range(len(s)):
            if s_sum + s[i] > 0:
                s_sum += s[i]
                ans += s_sum
            else:
                break
        return ans
satisfaction = [4, 3, 2]
a = Solution()
print(a.maxSatisfaction(satisfaction))