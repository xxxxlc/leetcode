# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        ans = 0

        for i in range(len(points)):
            k_num = {}
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0]:
                    k = float('inf')
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                k_num[k] = k_num.get(k, 0) + 1
                if k_num.get(k) > ans:
                    ans = k_num[k]
        
        return ans + 1
        


points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
a = Solution()
print(a.maxPoints(points))