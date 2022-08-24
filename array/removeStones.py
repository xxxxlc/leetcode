# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        stonesSet = []

        for i in range(len(stones)):
            connectStatuis = False
            idx = None
            for s in stonesSet:
                if self.isConnect(stones[i], s):
                    if connectStatuis == False:
                        s[0].add(stones[i][0])
                        s[1].add(stones[i][1])
                        connectStatuis = True
                        idx = stonesSet.index(s)
                        continue
                    else:
                        stonesSet[idx][0] = stonesSet[idx][0].union(s[0])
                        # print(stonesSet[idx][1])
                        # print(s[1])
                        # print(stonesSet[idx][1].union(s[1]))
                        stonesSet[idx][1] = stonesSet[idx][1].union(s[1])
                        stonesSet.remove(s)
            if connectStatuis == False:
                a = set()
                b = set()
                a.add(stones[i][0])
                b.add(stones[i][1])
                stonesSet.append([a, b])

        return len(stones) - len(stonesSet)

    def isConnect(self, stone, s):
        for row in s[0]:
            if stone[0] == row:
                return True
        for col in s[1]:
            if stone[1] == col:
                return True
        return False

stones = [[3,3],[4,4],[1,4],[1,5],[2,3],[4,3],[2,4]]

a = Solution()
print(a.removeStones(stones))
