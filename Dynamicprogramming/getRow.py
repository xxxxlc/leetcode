# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex):
            floor = []
            for j in range(0, i + 1):
                if j == 0:
                    floor.append(res[j])
                elif j == i:
                    floor.append(res[-1])
                else:
                    floor.append(res[j-1] + res[j])
            res = floor
        
        return res

rowIndex = 5
a = Solution()
print(a.getRow(rowIndex))