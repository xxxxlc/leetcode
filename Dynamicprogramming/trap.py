# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        n = len(height)

        leftMax = [height[0]] + [0] * (n - 1)

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))

        return ans


height = [1,6,0,0,0,6,7,9,3,4,7,4]
a = Solution()
print(a.trap(height))