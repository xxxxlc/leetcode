# 给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。

# 如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        ans = 0

        for i in range(m):
            for k in range(m):
                temp = []
                for j in range(m):
                    temp.append(grid[j][k])
                if temp == grid[i]:
                    ans += 1
        
        return ans

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

a = Solution()
print(a.equalPairs(grid))