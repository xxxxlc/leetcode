# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        res.append([1])
        for i in range(1, numRows):
            floor = []
            for j in range(0, i + 1):
                if j == 0:
                    floor.append(res[-1][j])
                elif j == i:
                    floor.append(res[-1][-1])
                else:
                    floor.append(res[-1][j-1] + res[-1][j])
            res.append(floor)
        
        return res



numRows = 5
a = Solution()
print(a.generate(numRows))