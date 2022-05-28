# 给你两个整数 x 和 y ，表示你在一个笛卡尔坐标系下的 (x, y) 处。同时，在同一个坐标系下给你一个数组 points ，其中 points[i] = [ai, bi] 表示在 (ai, bi) 处有一个点。当一个点与你所在的位置有相同的 x 坐标或者相同的 y 坐标时，我们称这个点是 有效的 。

# 请返回距离你当前位置 曼哈顿距离 最近的 有效 点的下标（下标从 0 开始）。如果有多个最近的有效点，请返回下标 最小 的一个。如果没有有效点，请返回 -1 。

# 两个点 (x1, y1) 和 (x2, y2) 之间的 曼哈顿距离 为 abs(x1 - x2) + abs(y1 - y2) 。

class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min = [-1, float("inf")]
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                d = abs(x - points[i][0]) + abs(y - points[i][1])
                if d < min[1]:
                    min[1] = d
                    min[0] = i
        return min[0]

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]

a = Solution()
print(a.nearestValidPoint(x, y, points))
