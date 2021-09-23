# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        while(i < len(intervals)):
            j = i + 1

            while(j < len(intervals)):
                if self.ismerge(intervals[j], intervals[i]):
                    intervals[i]= self.twomerge(intervals[j], intervals[i])
                    intervals.pop(j)
                    j = i + 1
                    continue

                j = j + 1
            i = i + 1
        
        return intervals
                    

    
    def ismerge(self, x1, x2):
        if x1[1] < x2[0] or x1[0] > x2[1]:
            return False
        else:
            return True
    
    def twomerge(self, x1, x2):
        return [min(x1[0],x2[0]), max(x1[1],x2[1])]



intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
a = Solution()
print(a.merge(intervals))
