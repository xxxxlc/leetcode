# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_rectangle_area = 0
        for row in range(len(matrix)):
            heights = [0]*len(matrix[0])
            for col in range(len(matrix[0])):
                if matrix[row][col] == '0':
                    heights[col] = 0
                    continue
                j = row
                while(matrix[j][col] != '0'):
                    j = j - 1
                    if j < 0:
                        break
                heights[col] = row - j
            if max_rectangle_area < self.largestRectangleArea(heights):
                max_rectangle_area = self.largestRectangleArea(heights)
        
        return max_rectangle_area
            

                
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
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(a.maximalRectangle(matrix))