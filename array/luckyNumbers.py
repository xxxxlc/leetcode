# 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

# 幸运数是指矩阵中满足同时下列两个条件的元素：

# 在同一行的所有元素中最小
# 在同一列的所有元素中最大

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        for i in range(len(matrix)):
        
            min_ele = min(matrix[i])
            min_index = matrix[i].index(min_ele)
           
            t = True
            for j in range(len(matrix)):
                if i == j:
                   continue
                if min_ele < matrix[j][min_index]:
                    t = False
                    break

            if t == True:
                ans.append(min_ele)

        return ans
        

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

a = Solution()
print(a.luckyNumbers(matrix))

