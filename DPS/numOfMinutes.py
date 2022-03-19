# 公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。

# 在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headID] = -1。题目保证从属关系可以用树结构显示。

# 公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。

# 第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，他的所有直属下属都可以开始传播这一消息）。

# 返回通知所有员工这一紧急消息所需要的 分钟数 。

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        self.ans = 0

        q = [headID]

        relationship = [[] for _ in range(0, n)]
        for i in range(0, len(manager)):
            if manager[i] >= 0:
                relationship[manager[i]].append(i)
        
        self.dfs(headID, informTime, relationship, 0)

        return self.ans

    def dfs(self, stuff, informTime, relationship, time):
        if informTime[stuff] == 0:
            if time > self.ans:
                self.ans = time
            return
        
        for i in relationship[stuff]:
            self.dfs(i, informTime, relationship, time + informTime[stuff])



n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

a = Solution()
print(a.numOfMinutes(n, headID, manager, informTime))