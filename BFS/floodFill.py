# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

# 最后返回经过上色渲染后的图像

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        q = []
        changecolor = image[sr][sc]
        image[sr][sc] = newColor
        q.append([sr, sc])

        paint = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while(q):
            cur = q.pop(0)

            for d in directions:
                x = cur[0] + d[0]
                y = cur[1] + d[1]

                if len(image) > x >= 0 and len(image[0]) > y >= 0:
                    if image[x][y] == changecolor and paint[x][y] == 0:
                        q.append([x, y])
                        image[x][y] = newColor
                        paint[x][y] = 1
                else:
                    continue
        
        return image


image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1 
newColor = 1

a = Solution()
print(a.floodFill(image, sr, sc, newColor))
