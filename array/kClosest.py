# 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。

# 这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)2 + (y1 - y2)2 ）。

# 你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        points = sorted(points, key=lambda x : x[0] ** 2 + x[1] ** 2, reverse=False)

        return points[:k]
        




points = [[1,3],[-2,2]]
k = 1

a = Solution()
print(a.kClosest(points, k))