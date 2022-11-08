# 给你两个字符串数组 creators 和 ids ，和一个整数数组 views ，所有数组的长度都是 n 。平台上第 i 个视频者是 creator[i] ，视频分配的 id 是 ids[i] ，且播放量为 views[i] 。

# 视频创作者的 流行度 是该创作者的 所有 视频的播放量的 总和 。请找出流行度 最高 创作者以及该创作者播放量 最大 的视频的 id 。

# 如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。
# 如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 id 。
# 返回一个二维字符串数组 answer ，其中 answer[i] = [creatori, idi] 表示 creatori 的流行度 最高 且其最流行的视频 id 是 idi ，可以按任何顺序返回该结果。

import heapq

class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        n = len(creators)

        c = {}
        d = {}

        for i in range(n):
            c[creators[i]] = c.get(creators[i], 0) + views[i]
            if creators[i] in d:
                if d[creators[i]][0] < views[i]:
                    d[creators[i]][0] = views[i]
                    d[creators[i]][1] = ids[i]
                elif d[creators[i]][0] == views[i]:
                    d[creators[i]][1] = min(d[creators[i]][1], ids[i])
            else:
                d[creators[i]] = []
                d[creators[i]].append(views[i])
                d[creators[i]].append(ids[i])
        
        ansName = []
        maxValue = 0
        for key, value in c.items():
            if value > maxValue:
                maxValue = value
                ansName = [[key, d[key][1]]]
            elif value == maxValue:
                ansName.append([key, d[key][1]])
        
        return ansName


creators = ["alice","bob","alice","chris"]
ids = ["one","two","three","four"]
views = [5,10,5,4]

a = Solution()
print(a.mostPopularCreator(creators, ids, views))
