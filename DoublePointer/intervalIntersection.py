# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。

# 返回这 两个区间列表的交集 。

# 形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。

# 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        n1 = len(firstList)
        n2 = len(secondList)
        p1 = 0
        p2 = 0

        ans = []

        while (p1 < n1 and p2 < n2):
            if firstList[p1][1] < secondList[p2][0]:
                p1 += 1
                continue
            if firstList[p1][0] > secondList[p2][1]:
                p2 += 1
                continue
            
            if firstList[p1][1] <= secondList[p2][1]:
                ans.append([max(firstList[p1][0], secondList[p2][0]), firstList[p1][1]])
                p1 += 1
                continue

            else:
                ans.append([max(firstList[p1][0], secondList[p2][0]), secondList[p2][1]])
                p2 += 1
                continue

        return ans
            




firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

a = Solution()
print(a.intervalIntersection(firstList, secondList))