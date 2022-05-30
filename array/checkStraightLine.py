# 给定一个数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if coordinates[0][0] - coordinates[1][0] != 0:
            k = (coordinates[0][1] - coordinates[1][1]) / float(coordinates[0][0] - coordinates[1][0])
            b = coordinates[0][1] - k * coordinates[0][0]

            for i in range(2, len(coordinates)):
                if coordinates[i][1] != k * coordinates[i][0] + b:
                    return False
            return True
        else:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True


coordinates = [[2,1],[4,2],[6,3]]

a = Solution()
print(a.checkStraightLine(coordinates))