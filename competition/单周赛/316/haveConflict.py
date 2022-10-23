# 给你两个字符串数组 event1 和 event2 ，表示发生在同一天的两个闭区间时间段事件，其中：

# event1 = [startTime1, endTime1] 且
# event2 = [startTime2, endTime2]
# 事件的时间为有效的 24 小时制且按 HH:MM 格式给出。

# 当两个事件存在某个非空的交集时（即，某些时刻是两个事件都包含的），则认为出现 冲突 。

# 如果两个事件之间存在冲突，返回 true ；否则，返回 false 。

from tracemalloc import start


class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        strat1 = event1[0].split(':')
        strat1 = int(strat1[0]) * 60 + int(strat1[1])
        end1 = event1[1].split(':')
        end1 = int(end1[0]) * 60 + int(end1[1])


        strat2 = event2[0].split(':')
        strat2 = int(strat2[0]) * 60 + int(strat2[1])
        end2 = event2[1].split(':')
        end2 = int(end2[0]) * 60 + int(end2[1])

        if end1 < strat2 or strat1 > end2:
            return False




        return True


event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]

a = Solution()
print(a.haveConflict(event1, event2))