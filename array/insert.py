# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        pre_mark = None
        next_mark = None
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0] and pre_mark is None:
                pre_mark = i
            if intervals[i][0] > newInterval[1]:
                next_mark = i
                break
        if next_mark is None and pre_mark is None:
            intervals.append(newInterval)
            return intervals
        elif next_mark is None and pre_mark != None:
            next_mark = len(intervals)
        elif pre_mark == next_mark:
            intervals.insert(pre_mark, newInterval)
            return intervals
        
        new_up = max(newInterval[1], intervals[next_mark - 1][1])
        new_low = min(newInterval[0], intervals[pre_mark][0])
        intervals.insert(next_mark, [new_low, new_up])
        intervals = intervals[0:pre_mark] + intervals[next_mark:]
        return intervals
        

intervals =  [[1,5]]
newInterval = [5,7]

a = Solution()
print(a.insert(intervals, newInterval))