# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = []
        stack_index = []
        left = [-1]
        right = [len(heights)]
        stack.append(heights[0])
        stack_index.append(0)
        j = 0
        for index in range(1, len(heights)):
            if heights[index] > stack[j]:
                stack.append(heights[index])
                stack_index.append(index)
                j = j + 1
            else:
                while(stack[j] >= heights[index]):
                    stack.pop()
                    stack_index.pop()
                    j = j - 1
                    if j == -1:
                        break
                stack.append(heights[index])
                stack_index.append(index)
                j = j + 1
            if len(stack) == 1:
                left.append(-1)
            else:
                left.append(stack_index[-2])

        stack = []
        stack_index = []
        stack.append(heights[len(heights)-1])
        stack_index.append(len(heights)-1)
        j = 0
        for index in range(len(heights)-2, -1, -1):
            if heights[index] > stack[j]:
                stack.append(heights[index])
                stack_index.append(index)
                j = j + 1
            else:
                while(stack[j] >= heights[index]):
                    stack.pop()
                    stack_index.pop()
                    j = j - 1
                    if j == -1:
                        break
                stack.append(heights[index])
                stack_index.append(index)
                j = j + 1
            if len(stack) == 1:
                right.append(len(heights))
            else:
                right.append(stack_index[-2])
        right.reverse()
        #print(right)
        #print(left)
        max_area = 0
        for index in range(len(heights)):
            if max_area < (right[index] - left[index] - 1)*heights[index]:
                max_area = (right[index] - left[index] - 1)*heights[index]
        return max_area


a = Solution()
heights = [1,1]
print(a.largestRectangleArea(heights))