# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。

# 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        for i in range(len(rectangles)):
            if i == 0:
                maxLeft = [i, rectangles[i][0]]
                maxDown = [i, rectangles[i][1]]
                maxRight = [i, rectangles[i][2]]
                maxUp = [i, rectangles[i][3]]
            else:
                if maxLeft[1] > rectangles[i][0]:
                    maxLeft = [i, rectangles[i][0]]
                elif maxLeft[1] == rectangles[i][0]:
                    if rectangles[maxLeft[0]][1] > rectangles[i][1]:
                        maxLeft = [i, rectangles[i][0]]

                if maxDown[1] > rectangles[i][1]:
                    maxDown = [i, rectangles[i][1]]
                elif maxDown[1] == rectangles[i][1]:
                    if rectangles[maxDown[0]][0] > rectangles[i][0]:
                        maxDown = [i, rectangles[i][1]]

                if maxRight[1] < rectangles[i][2]:
                    maxRight = [i, rectangles[i][2]]
                elif maxRight[1] == rectangles[i][2]:
                    if rectangles[maxRight[0]][3] < rectangles[i][3]:
                        maxRight = [i, rectangles[i][2]]

                if maxUp[1] < rectangles[i][3]:
                    maxUp = [i, rectangles[i][3]]
                elif maxUp[1] == rectangles[i][3]:
                    if rectangles[maxUp[0]][2] < rectangles[i][2]:
                        maxUp = [i, rectangles[i][3]]

        if maxLeft[0] != maxDown[0]:
            return False
        if maxRight[0] != maxUp[0]:
            return False
        
        leftDown = [maxLeft[1], maxDown[1]]
        rightUp = [maxRight[1], maxUp[1]]
        
        maxArea = (rightUp[0] - leftDown[0]) * (rightUp[1] - leftDown[1])
        area = 0
        for i in range(len(rectangles)):
            area += (rectangles[i][2] - rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1])
        if area != maxArea:
            return False
        
        row = rightUp[1] - leftDown[1] + 1
        col = rightUp[0] - leftDown[0] + 1

        area = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(len(rectangles)): 
            for m in range(rectangles[i][0], rectangles[i][2]):
                for n in range(rectangles[i][1], rectangles[i][3]):
                    y = m - leftDown[0]
                    x = n - leftDown[1]
                    if area[x][y] == 1:
                        return False
                    else:
                        area[x][y] = 1
        return True

                
            
rectangles = [[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]]

a = Solution()
print(a.isRectangleCover(rectangles))