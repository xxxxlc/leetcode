# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
from decimal import MIN_ETINY


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        ans = float('inf')

        for i in range(0, len(timePoints) - 1):
            for j in range(i + 1, len(timePoints)):
                t = self.count(timePoints[i], timePoints[j])
                if t < ans:
                    ans = t
                if ans == 0:
                    return ans
        return ans
    
    def count(self, x, y):
        tempx = x.split(':')
        tempy = y.split(':')
        hourx = int(tempx[0])
        minutex = int(tempx[1])
        houry = int(tempy[0])
        minutey = int(tempy[1])

        hour = hourx - houry
        minute = minutex - minutey



        return min(abs(hour * 60 + minute), 24 * 60 - abs(hour * 60 + minute))


timePoints = ["23:59","00:00"]

a = Solution()
print(a.findMinDifference(timePoints))