# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        countpoint = [0 for _ in range(numCourses)]
        map = dict()
        for i in range(numCourses):
            map[i] = []
        for course in prerequisites:
            map[course[1]].append(course[0])
            countpoint[course[0]] += 1
        q = []
        for i in range(numCourses):
            if countpoint[i] == 0:
                q.append(i)
        if not q:
            return False
        visited = 0
        while(q):
            visited += 1
            cur = q.pop(0)
            for v in map[cur]:
                countpoint[v] -= 1
                if countpoint[v] == 0:
                    q.append(v)
        return visited == numCourses


    

numCourses = 2
prerequisites = [[1,0],[0,1]]

a = Solution()
print(a.canFinish(numCourses, prerequisites))