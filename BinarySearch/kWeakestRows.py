# 给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

# 请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。

# 如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。

# 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        visited = [0] * len(mat)
        ans = []
        for m in range(0, k):
            sum_min = len(mat[0])
            for n in range(0, len(mat)):
                if visited[n] == 0:
                    idx_min = n
                    break
            for i in range(0, len(mat)):
                if visited[i] == 1:
                    continue
                c = sum(mat[i])
                if sum_min > c:
                    sum_min = c
                    idx_min = i
            visited[idx_min] = 1
            ans.append(idx_min)
        return ans


mat = [[1,0],[1,0],[1,0],[1,1]]
k = 4

a = Solution()

print(a.kWeakestRows(mat, k))
