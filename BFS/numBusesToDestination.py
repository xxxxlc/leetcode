# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。

# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。

# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。

from collections import defaultdict, deque


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        # if source == target:
        #     return 0
            
        # busMap = {}
        # for i in range(len(routes)):
        #     for station in routes[i]:
        #         if station in busMap:
        #             busMap[station].append(i)
        #         else:
        #             busMap[station] = [i]
        
        # print(busMap)

        # 单方向BFS；超出时间限制
        # q = []
        # q.append(source)
        # visited = set()
        # visited.add(source)
        # isArrive = False
        # numBus = 0

        # while(q):
        #     numBus += 1
        #     for i in range(len(q)):
        #         curStation = q.pop(0)

        #         for bus in busMap[curStation]:
        #             for arriveStation in routes[bus]:
        #                 if arriveStation == target:
        #                     isArrive = True
        #                     break

        #                 if arriveStation not in visited:
        #                     visited.add(arriveStation)
        #                     q.append(arriveStation)
            
        #     if isArrive == True:
        #         break

        # 双向BFS
        # isArrive = False
        # numBus = 0
        # visitedSource = set()
        # visitedTarget = set()
        # visitedSource.add(source)
        # visitedTarget.add(target)

        # qSource = [source]
        # qTarget = [target]

        # while(qSource and qTarget):
        #     numBus += 1

        #     for i in range(len(qSource)):
        #         curStation = qSource.pop(0)

        #         if curStation not in busMap.keys():
        #             continue

        #         for bus in busMap[curStation]:
        #             for arriveStation in routes[bus]:
        #                 if arriveStation not in visitedSource:
        #                     visitedSource.add(arriveStation)
        #                     qSource.append(arriveStation)
            
        #     if visitedSource.intersection(visitedTarget):
        #         isArrive = True
        #         break


        #     numBus += 1

        #     for i in range(len(qTarget)):
        #         curStation = qTarget.pop(0)

        #         if curStation not in busMap.keys():
        #             continue

        #         for bus in busMap[curStation]:
        #             for arriveStation in routes[bus]:
        #                 if arriveStation not in visitedTarget:
        #                     visitedTarget.add(arriveStation)
        #                     qTarget.append(arriveStation)

        #     if visitedSource.intersection(visitedTarget):
        #         isArrive = True
        #         break
        
        # if isArrive == True:
        #     return numBus
        # else:
        #     return -1

        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                if stop in stations:
                    stations[stop].add(i)
                else:
                    stations[stop] = set(i)
        # 每个公交车线路可以到达的车站
        routes = [set(x) for x in routes]

        q = deque([(source, 0)])
        # 已经乘坐了的公交车
        buses = set()
        # 已经到达了的车站
        stops = {source}
        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost
            # 当前车站中尚未乘坐的公交车
            for bus in stations[pos] - buses:
                # 该公交车尚未到达过的车站
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1


routes = [[1,2,7],[3,6,7]]
source = 1
target = 6

a = Solution()
print(a.numBusesToDestination(routes, source, target))
