# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

# 如果小镇法官真的存在，那么：

# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。

# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        people = [[] for _ in range(n)]
        trustpeople = [[] for _ in range(n)]

        for i in range(len(trust)):
            people[trust[i][1] - 1].append(trust[i][0] - 1)
            trustpeople[trust[i][0] - 1].append(trust[i][1] - 1)
        
        for i in range(n):
            if len(people[i]) == n - 1 and len(trustpeople[i]) == 0:
                return i + 1
        return -1 

n = 2
trust = [[1,2]]

a = Solution()
print(a.findJudge(n, trust))
