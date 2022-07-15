# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preCourse = [[] for _ in range(numCourses)]

        for k in prerequisites:
            preCourse[k[0]].append(k[1])
        
        firstCourse = [i for i in range(len(preCourse)) if len(preCourse[i]) == 0]
        
        if not firstCourse:
            return []
        
        isFinish = [0] * numCourses
        finishOrder = []

        for i in range(len(firstCourse)):
            isFinish[firstCourse[i]] = 1
    
        while(firstCourse):
            cur = firstCourse.pop(0)
            finishOrder.append(cur)
            for i in range(len(preCourse)):
                if cur in preCourse[i]:
                    preCourse[i].remove(cur)
                if len(preCourse[i]) == 0 and isFinish[i] == 0:
                    isFinish[i] = 1
                    firstCourse.append(i) 
        
        if len(finishOrder) == numCourses:
            return finishOrder
        else:
            return []
            



numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

a = Solution()
print(a.findOrder(numCourses, prerequisites))