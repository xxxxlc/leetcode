# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x : (x[0], x[1]))
        right = float("-inf")
        remove = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= right:
                right = intervals[i][1]
                continue
            else:
                if right > intervals[i][1]:
                    right = intervals[i][1]
                remove += 1
        return remove


intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
a = Solution()
print(a.eraseOverlapIntervals(intervals))

